from django.shortcuts import render

# Create your views here.
def show_skills(request):
    return render(request, 'skills/_skills.html')