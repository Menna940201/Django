from django.shortcuts import render

# Create your views here.
def show_education(request):
    return render(request, 'education/_education.html')