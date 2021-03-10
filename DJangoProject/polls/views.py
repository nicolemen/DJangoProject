from django.shortcuts import render

# Create your views here.

class MainView(generic.DetailView):
    template_name = 'polls/main.html'

class LoginView(generic.DetailView):
    template_name = 'polls/login.html'
