from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all();
    print(blog_posts)
    return render(request,"blog_app/index.html", {"blogs": blog_posts})