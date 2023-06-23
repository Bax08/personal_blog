from django.shortcuts import render

# Create your views here.
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'personal_blogs/home.html', {'posts': posts})
