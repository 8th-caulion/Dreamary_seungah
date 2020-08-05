from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def introduce(request):
    return render(request, 'introduce.html')