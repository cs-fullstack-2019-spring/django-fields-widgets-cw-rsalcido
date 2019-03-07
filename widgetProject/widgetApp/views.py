from django.shortcuts import render
from django.http import HttpResponse
from .forms import supeHeroForm


# Create your views here.

def index(request):
    print('error')
    return render(request, 'widgetApp/index.html')


def residency_application(request):
    if (request.method=="POST"):
        print('error')
        form = supeHeroForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
        else:
            print(form.errors)
            print("error")
    return render(request, 'widgetApp/residency_application.html', {'form': supeHeroForm})


def thankyou_page(request):
    return HttpResponse('test thank you ')
