from django.shortcuts import render
from .models import BlogPost, Like

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all()
    popular_posts = BlogPost.top_liked_posts(BlogPost)
    return render(request,"blog_app/index.html", {"blogs": blog_posts,"top_posts":popular_posts})