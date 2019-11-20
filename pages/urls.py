# pages/urls.py
from django.urls import path

# from .views import HomePageView
from . import views

urlpatterns = [
    path('', views.homepage, name='Home Page')
]
