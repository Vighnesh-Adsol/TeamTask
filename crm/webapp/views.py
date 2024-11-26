from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateTaskForm, GroupForm, loginGroupForm

from django.contrib.auth.models import auth, Group
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required


from .models import Task_rec

from django.contrib import messages



# - Homepage 

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'webapp/index.html')
    else:
        show = not request.user.groups.exists()
        context={'show':show}
        return render(request, 'webapp/ifLoginHome.html', context=context)
        


# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my-login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):
  
    if request.user.is_authenticated:
        if request.user.groups.exists():
            
        # if user in any group exists
            for group in request.user.groups.all():
                group__name= group.name
            group = Group.objects.get(name=group__name)
            
            group_members= group.user_set.all()

            if group in request.user.groups.all():
            # User is authenticated and belongs to the specified group
               
                my_tasks=Task_rec.objects.filter(status=False, group= group)
                finished_tasks=Task_rec.objects.filter(status=True, group= group)
        
                classn= "btn btn-danger"
                
        
                context = {'tasks':my_tasks,
                            'classn':classn,
                            'fintask':finished_tasks,
                            'gName': group__name,
                            'members':group_members,
                            }
           
                return render(request, 'webapp/dashboard.html', context=context)
            
        else:
            # User is authenticated but not in the group
            return redirect("LoginGrp")
    else:
        # User is not authenticated
        
        
        return redirect("my-login")


# - Create a Task

@login_required(login_url='my-login')
def create_task(request):
    form= CreateTaskForm()
    if request.method=='POST':
        form= CreateTaskForm(request.POST)
        
        if form.is_valid():
              # Get the user's group (assuming the user belongs to only one group for simplicity)
            user_group = request.user.groups.first()

            # Create the task and associate it with the user's group
            task = form.save(commit=False)
            task.group = user_group
            task.creator= request.user
            task.save()
            return redirect("dashboard")
    context = {'form':form}
    return render(request, 'webapp/create-task.html', context=context)    




# - Update a record 

@login_required(login_url='my-login')
def update_task(request, pk):

    task = Task_rec.objects.get(id=pk)

    form = UpdateTaskForm(instance=task)

    if request.method == 'POST':

        form = UpdateTaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Task was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update-task.html', context=context)


# - View a singular record

@login_required(login_url='my-login')
def viewTask(request, pk):
    all_tasks= Task_rec.objects.get(id=pk)
    t_stat= all_tasks.status
    context ={'task':all_tasks,
              't_stat':t_stat}
    return render(request, 'webapp/view-Task.html', context=context)



# - Delete a record

@login_required(login_url='my-login')
def delete_task(request, pk):

    task = Task_rec.objects.get(id=pk)

    task.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")


# - delete all tasks
@login_required(login_url='my-login')
def deleteAll_task(request):
    allTask = Task_rec.objects.filter(status=True)
    
    allTask.delete()
    messages.success(request, "All completed task were deleted!")
    
    return redirect("dashboard")


# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")


# change status
@login_required(login_url='my-login')
def chg_status(request, pk):
    
    task =Task_rec.objects.get(id=pk)
    if task.status == False:
        task.status= True
    else:
        task.status= False
    task.save()
    return redirect("dashboard")

# - create a group 
@login_required(login_url='my-login')
def create_grp(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('joinGrp')
        else:
            messages.warning(request, "Group already exists!")
            return render(request, 'webapp/createGrp.html', {'form': form})
    else:
        form = GroupForm()
        return render(request, 'webapp/createGrp.html', {'form': form})


# login a group 
@login_required(login_url='my-login')
def login_grp(request):
    return redirect("joinGrp")


# join a group 
@login_required(login_url='my-login')
def join_grp(request):
    if request.method == 'POST':
        # Retrieve the entered group name from the form
        group_name = request.POST.get('name')
        request.session['group_name'] = group_name
        try:
            # Get the group object based on the entered name
            group = Group.objects.get(name=group_name)

            # Get the currently logged-in user
            user = request.user

            # Add the user to the group
            group.user_set.add(user)

            # Success message
            messages.success(request, f"You have successfully joined the group '{group_name}'!")
            return redirect('dashboard')# Redirect to dashboard after successful join

        except Group.DoesNotExist:
            # Handle case where the group doesn't exist
            messages.error(request, f"Group '{group_name}' does not exist.")

    # Render the join group form on GET request
    form = loginGroupForm()
    return  render(request, 'webapp/joinGrp.html', {'form': form}) 

# - Leave Group 
@login_required(login_url='my-login')
def leave_grp(request):
    # if request.method == 'POST':
    #     # Retrieve the entered group name from the form
    #     group_name = request.POST.get('name')

    #     try:
    #         # Get the group object based on the entered name
    #         group = Group.objects.get(name=group_name)

    #         # Get the currently logged-in user
    #         user = request.user

    #         # delete the user to the group
    #         group.user_set.remove(user)

    #         # Success message
    #         messages.success(request, f"You have successfully left the group '{group_name}'!")
    #         return redirect('dashboard')  # Redirect to dashboard after successful join

    #     except Group.DoesNotExist:
    #         # Handle case where the group doesn't exist
    #         messages.error(request, f"Group '{group_name}' does not exist.")

    # # Render the join group form on GET request
    # form = loginGroupForm()
   
    # return render(request, 'webapp/leaveGrp.html', {'form': form})
    
    if request.user.groups.exists():
        for group in request.user.groups.all():
            g= Group.objects.get(name=group.name)
            g.user_set.remove(request.user)
            messages.success(request, f"You have successfully left the group '{group.name}'!")
             
            
        return redirect("dashboard")
    else:
        messages.error(request, f"You're not in any group!")
        
        return redirect("joinGrp")