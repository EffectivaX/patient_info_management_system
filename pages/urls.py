# pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.homepage, name='Home Page')
    path('', views.homepage, name='Home')
]
