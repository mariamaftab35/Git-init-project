from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Welcom to Home Page</h1>")

def index(request):
    return render(request,"index.html")    