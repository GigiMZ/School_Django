from django.shortcuts import render
from .models import Post

def home(request):
    post = Post.objects.first()
    post
    context = {'post': post}
    return render(request, 'home.html', context=context)