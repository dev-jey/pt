from django.shortcuts import render
from project.models import About, Skill, Project, ProjectType


def get_home(request):
    project_types = ProjectType.objects.all()
    about = About.objects.all().first()
    return render(request, 'index.html', {"about": about, "project_types": project_types})
