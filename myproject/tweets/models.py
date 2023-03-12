from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=10,unique=True,default=True)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=10,blank=False,default=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
class Tweet(models.Model):
    username = models.CharField(max_length=10)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'tweets'

class UserProfile(models.Model):
    user = models.CharField(max_length=20,default=True)
    mobile = models.CharField(max_length=20,default=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)

    class Meta:
        app_label = 'tweets'
