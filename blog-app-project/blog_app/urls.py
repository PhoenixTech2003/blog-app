from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
   path("<int:postId>/like/", views.like_blog_post,name='like_blog_post'),
   path("<int:postId>/", views.blog_post, name='post'),
   path("signup/",views.signup,name = 'signup')
]
