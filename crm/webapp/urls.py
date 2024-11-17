
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-task', views.create_task, name="create-task"), 
    
    path('viewTask/<int:pk>', views.viewTask, name="viewTask"),
    
    path('updateTask/<int:pk>', views.update_task, name='update-task'),
    
    path('deleteTask/<int:pk>', views.delete_task, name='delete-task'),
    
    path('chg-status/<int:pk>', views.chg_status, name="chg-status"), 
    
    path('deleteAll_task', views.deleteAll_task, name='deleteAll_task'),

    path('crtGrp', views.create_grp, name="crtGrp"),
    
    path('LoginGrp', views.login_grp, name="LoginGrp"),
    
    path('joinGrp', views.join_grp, name="joinGrp"),
    
    path('leaveGrp', views.leave_grp, name="leaveGrp")

]






     