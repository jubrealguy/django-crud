from socket import fromshare
from django import forms
from .models import Post

class PostForm(forms):
    class Meta:
        model = Post
        fields = "__all__"