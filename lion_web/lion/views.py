from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = []
    return render(request, "lion/home.html", {'title': "index"})

def facerec(request):
    return render(request, "lion/facerec.html", {'title': "face"})
# Create your views here.
