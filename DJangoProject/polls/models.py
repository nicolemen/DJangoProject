from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    username= models.CharField(max_length=200, default=None)
    password = models.CharField(max_length=50, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.username

class Posts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=500, default=None)
    date = models.DateTimeField(max_length=50, default=None)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.content
