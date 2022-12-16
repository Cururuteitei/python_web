from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, "/home/lab-626465/tmp/python_web/sgt/hello/templates/index.html")
def jayan (request):
	return HttpResponse("o u jayan btl")
def gus(request):
	return HttpResponse("o u gus btl")
def greet(request , name):
	return render(request,"hello/greet.html" ,
	{"name":name.capitalize()})



