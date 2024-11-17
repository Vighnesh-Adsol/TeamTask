from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .models import Task_rec

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2','email']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    
# - Create a group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        
class loginGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


# - Create a task

class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Task_rec
        fields = ['task_name', 'description' ,'creator']


# - Update a record

class UpdateTaskForm(forms.ModelForm):

    class Meta:

        model = Task_rec
        fields = ['task_name' , 'description']
        
