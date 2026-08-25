from django.shortcuts import render

# Create your views here.
def show_experience(request):
    return render(request, 'work/_work.html')