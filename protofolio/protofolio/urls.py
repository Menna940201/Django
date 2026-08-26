"""
URL configuration for protofolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proto.views import write_home
from about.views import show_about_me
from education.views import show_education
from skills.views import show_skills
from work.views import show_experience
from projects.views import show_all_projects, show_projects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', write_home, name='home'),
    path('show_about_me/', show_about_me, name='about'),
    path('show_education/', show_education, name='education'),
    path('show_skills/', show_skills, name='skills'),
    path('show_experience/', show_experience, name='experience'),
    path('project/<int:num>', show_projects, name = 'project'),
    path('project/', show_all_projects, name = 'projects'),
]
