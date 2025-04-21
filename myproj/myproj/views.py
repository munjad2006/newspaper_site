from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



def trail(request):
    return render(request, 'trial.html')


def home(request):
    return HttpResponse("This is Home Page")


def about(request):
    return HttpResponse("This is About Page")
