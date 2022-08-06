from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='latest-posts'),
    path("posts/", views.allposts, name="all-posts"),
    path("posts/<slug:slug>/", views.post_detail, name="post-detail"),
]
