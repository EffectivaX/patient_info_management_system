from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

def homepage(request):
    template_name = 'home.html'

    context = {
        "title" : "Home Page"
    }

    return render(request, "home.html", context)
