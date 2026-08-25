from django.shortcuts import render
from django.http import HttpResponse

def write_home(request):
    return render(request, 'proto/home.html')
