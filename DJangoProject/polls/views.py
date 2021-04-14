from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Posts, Users
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.

def main_view(request):
    template = loader.get_template('polls/main.html')
    latest_post_list = Posts.objects.order_by('date')
    context = {
    'post_list' : latest_post_list,
    }
    print(latest_post_list)
    return HttpResponse(template.render(context, request))

def user_view(request):
    template = loader.get_template('polls/user.html')
    user_list = Users.objects.order_by('username')
    context = {
    'user_list' : user_list,
    }
    return HttpResponse(template.render(context, request))
