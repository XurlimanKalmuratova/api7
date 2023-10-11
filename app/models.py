from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.username


    
class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateField(auto_now=True)
    end_data = models.DateField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner')
    members = models.ManyToManyField(CustomUser, related_name='members')
    def __str__(self):
        return self.title
    

class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    deadline_date = models.DateField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE )
    assigned_to = models.CharField(max_length=256)
    completed = models.DateField(default=False)
    def __str__(self):
        return self.title




