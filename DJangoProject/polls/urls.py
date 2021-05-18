from django.urls import path
from . import views

# connects to two different views

urlpatterns = [
    path('', views.main_view, name="index"),
    path('user/', views.user_view, name="user"),
    path('<int:post_id>/upvote/', views.upvote, name="upvote"),
    path('<int:post_id>/downvote/', views.downvote, name="downvote"),
    path('post/', views.make_post_view, name="post"),
    path('submit/', views.submit, name="submit"),

    ]
