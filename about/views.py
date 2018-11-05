from django.shortcuts import render
from about.models import Post
from portfolio.models import Project

def new_view(request):
    posts = Post.objects.all() 
    projects = Project.objects.all()
    
    return render(request, 'about/home.html', {'posts': posts,'projects':projects})