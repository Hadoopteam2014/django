from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
