from django.shortcuts import render

# Create your views here.
def show_about_me(request):
    return render(request, 'about/about_me.html')