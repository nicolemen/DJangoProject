from django.db import models

# Create your models here.


class Users(models.Model):
    posts = models.ForeignKey('Posts',on_delete=models.CASCADE ,)


class Posts(model.Model):
