from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<center><h1>Hello world</h1></center>")

def page1(request):
    return HttpResponse("<marquee><h1>Hello Buddy</h1></marquee>")

def page2(request):
    return render(request,'first_html.html')