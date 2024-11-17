from django.db import models
from django.contrib.auth.models import Group


class Task_rec(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)

    task_name= models.CharField(max_length=500)
    
    description= models.CharField(max_length=700)
    
    status= models.BooleanField(default=False)
    
    creator=models.CharField(max_length=50, null=True)
    
    
    
    


    def __str__(self):

        return self.task_name













