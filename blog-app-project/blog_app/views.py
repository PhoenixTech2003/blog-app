from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Like

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all()
    popular_posts = BlogPost.top_liked_posts(BlogPost)
    return render(request,"blog_app/index.html", {"blogs": blog_posts,"top_posts":popular_posts})

def blog_post(request, postId):
    post = get_object_or_404(BlogPost, pk=postId)
    return render(request,"blog_app/blogPost.html", {"post":post})