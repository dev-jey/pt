from django.shortcuts import render
from project.models import About, Skill, Project, ProjectType


def get_home(request):
    return render(request, 'index.html')

def get_project(request, id):
    return render(request, 'project-view.html')
