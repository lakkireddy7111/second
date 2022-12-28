from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def madhav(request):
    return HttpResponse('<h2>This is app1 madhav view</h2>')
