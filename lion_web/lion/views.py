from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = []
    return render(request, "lion/home.html", {'title': "index"})
# Create your views here.
