from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
# Create your views here.
# projects = [
#     {'num':1, 'title':'Smart City Data Analysis System', 'description':'Designed a system to analyze traffic, accidents, and resource consumption data. Applied machine learning techniques to predict issues and optimize services'},
#     {'num':2, 'title':'Restaurant Rating Prediction Website', 'description':'Built a web application to predict restaurant ratings based on user inputs. Implemented machine learning models for accurate predictions'},
#     {'num':3, 'title':'Travel Website', 'description':'Developed a web platform for planning and showcasing travel trips. Focused on front-end design and user-friendly navigation'},
#     {'num':4, 'title':'Sudoku Game', 'description':"A classic Sudoku game where players can solve 9×9 Sudoku puzzles by filling in the empty cells with numbers from 1 to 9. The game validates the player's input and provides an interactive and challenging puzzle-solving experience."}
# ]
not_found = "Project not found"

def show_all_projects(request):
    projects = Projects.get_all_projects()
    return render(request, 'projects/_projects.html', context={'projects':projects})

def show_projects(request, id):
    # for project in projects:
    #     if project['id'] == id:
    #         return render(request, 'projects/detail.html' ,context={'project':project})
    # else:
    #     return HttpResponse(not_found)
    project = Projects.get_specific_project(id)
    return render(request, 'projects/detail.html', context={'project':project})
