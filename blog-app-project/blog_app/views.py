from django.shortcuts import render, get_object_or_404,redirect
from .models import BlogPost, Like
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all()
    popular_posts = BlogPost.top_liked_posts(BlogPost)
    return render(request,"blog_app/index.html", {"blogs": blog_posts,"top_posts":popular_posts})

def blog_post(request, postId):
    post = get_object_or_404(BlogPost, pk=postId)
    return render(request,"blog_app/blogPost.html", {"post":post})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email,password=password)
            user.save()
            return redirect('login')
    return render(request,'registration/signup.html')

@login_required
def like_blog_post(request, postId):
    post = get_object_or_404(BlogPost, pk = postId)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post', postId = postId)