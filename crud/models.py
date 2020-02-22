from django.db import models
from django.contrib.auth.models import User
from enum import Enum

# Create your models here.
class UserAccount(models.Model):
    name = models.CharField("Name",max_length=255)
    email = models.EmailField(blank=False,null=False)
    phone = models.CharField(max_length=50,blank=True,null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    usercreatedAt = models.DateTimeField("Created at", auto_now_add=True)
    
    def __str__(self):
        return self.name()

class MasterRole(models.Model):
    ActiveRoleChoices = (
        ('Active', 'A'),
        ('NotActive', 'N'),
    )
    name_role = models.CharField("Name Role",max_length=255)
    kode_role = models.CharField("Kode Role",max_length=20)
    description = models.TextField(blank=True,null=True)
    active = models.CharField(max_length=10,choices=ActiveRoleChoices,default='A',)
    createdAt = models.DateTimeField("Created at",auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_role()