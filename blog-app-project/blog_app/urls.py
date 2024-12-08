from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
   path("<int:postId>", views.blog_post, name="post")
   path("signup/",views.signup,name = 'signup')
]
