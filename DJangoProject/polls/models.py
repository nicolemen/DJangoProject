from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    # basic information relating to the "Reddit" post
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=500, default=None)
    date = models.DateTimeField(max_length=50, default=None)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.content
