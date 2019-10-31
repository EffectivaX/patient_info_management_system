# pages/urls.py
from django.urls import path

# from .views import HomePageView
from . import views

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', views.customhomepage, name="home"),
]