from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return HttpResponse('<h2><b>This is my second view</h2></b>')
