from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    verse = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Comment(models.Model):
    content =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Like(models.Model):
    post_id = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)