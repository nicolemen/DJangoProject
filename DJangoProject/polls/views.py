from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

# each view goes to one template

# main view is the main "Reddit" page with all of the posts
def main_view(request):
    if request.POST:
            if 'inputUsername' in request.POST.keys():
                user = authenticate(username=request.POST['inputUsername'],password=request.POST['inputPassword'])
                if user is not None:
                    login(request,user)
                else:
                    inputPassword
            elif 'logout'in request.POST.keys():
                logout(request)
    if request.user.is_authenticated:
        loggedIn = True
    else:
        loggedIn = False
    # views find models and retrieve the data, putting data in context and then sending to respective template
    template = loader.get_template('polls/main.html')
    latest_post_list = Posts.objects.order_by('-date')
    context = {
    'post_list' : latest_post_list,
    }
    print(latest_post_list)
    return HttpResponse(template.render(context, request))

# user view is the list of users that have created posts
def user_view(request):
    template = loader.get_template('polls/user.html')
    user_list = User.objects.order_by('username')
    context = {
    'user_list' : user_list,
    }
    return HttpResponse(template.render(context, request))

# make post view is where Reddit users can add to chain of posts
def make_post_view(request):
    template = loader.get_template('polls/post.html')
    return HttpResponse(template.render({}, request))

def submit(request):
    if request.method == "POST":
        thisUser = User.objects.get(username = request.POST['userPosting'])
        newPost = Posts(
            content = request.POST['newContent'],
            user = thisUser,
            date = timezone.now(),
        )
    newPost.save()
    return HttpResponseRedirect(reverse('index'))

# upvote and downvote functions that increment by one

def upvote(request, post_id):
    post = Posts.objects.get(pk=post_id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('index'))

def downvote(request, post_id):
    post = Posts.objects.get(pk=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('index'))
