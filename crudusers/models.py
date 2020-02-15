from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userpost(models.Model):
    name = models.CharField("Name",max_length=255)
    email = models.EmailField(blank=False,null=False)
    phone = models.CharField(max_length=50,blank=True,null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    usercreatedBy = models.ForeignKey(User,related_name='user_created_by',on_delete=models.CASCADE)
    usercreatedAt = models.DateTimeField("Created at", auto_now_add=True)

    def __str__(self):
        return self.name()