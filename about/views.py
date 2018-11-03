from django.shortcuts import render
from .models import About

# Create your views here.
def Home(request):
    return render(request, 'about/home.html')