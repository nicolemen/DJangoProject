from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name="index"),
    path('user/', views.user_view, name="user"),


    ]
