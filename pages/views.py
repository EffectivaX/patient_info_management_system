from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
# Create your views here.


# class HomePageView(TemplateView):
#     template_name = 'home.html'
#
# def homepage(request):
#     template_name = 'home.html'
#
#     context = {
#         "title" : "Home Page"
#     }
#
#     return render(request, "home.html", context)

def homepage(request):
    template_name = 'home.html'

    context = {
        'title': 'HealthNet Dashboard',
        'project_name' : 'ProHealthnet',
        'creator' : 'Andile XeroxZen'
    }

    return render(request, 'pages/home.html', context)

def request_updates(request):
    form = ProgressUpdateForm()
    if request.method == 'POST':
        form = ProgressUpdateForm(request.POST)
        if form.is_valid():
            # Process and clean the data
            request_email = ProgressUpdate.objects.create(
                request_email = form.cleaned_data.get('request_email')
            )

            request_email.save()
            messages.success(request, 'Email Sent successfully!', extra_tags='alert')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Notification updates failed!', extra_tags='alert')
    else:
        form = ProgressUpdateForm()

    context = {
        'form' : form,
        # 'button' : 'Add Member',
        # 'project_name' : 'ProMed HealthNet Inc',
        # 'title' : 'Add New Staff Member'
    }

    return render(request, '/', context)
