from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }