from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('<h1> hello </h1>')

def about(request):
    return HttpResponse('<h1> about us </h1>')