from django.urls import path
from . import views

urlpatterns = [
    #Paths del gestor
    path('', views.Home, name="home"),
]
