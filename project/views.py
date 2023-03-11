from django.shortcuts import render
from project.models import About, Skill, Project, ProjectType, MyClient


def get_home(request):

    projects = Project.objects.filter(active=True)
    project_types = ProjectType.objects.all()
    clients = MyClient.objects.all()
    about = About.objects.first()


    all_projects = []
    all_project_types = []
    all_clients = []

    for project in projects:
        all_projects.append(
            {
                "id": project.pk,
                "title": project.title,
                "image": project.image,
                "proj_type": project.project_type.non_verbose_name,
            }
        )
    for typ in project_types:
        all_project_types.append(
            {
                "id": typ.pk,
                "name": typ.name,
                "joined_name": typ.non_verbose_name,
            }
        )
    for client in clients:
        all_clients.append(
            {
                "id": client.pk,
                "name": client.name,
                "image": client.logo_url,
            }
        )
    about_data = {
        "instagram": about.instagram,
        "dribble": about.dribble,
        "behance": about.behance,
        "upwork": about.upwork,
        "intro": about.intro
    }
    return render(request, 'index.html', context={
        "projects": all_projects,
        "project_types":all_project_types,
        "clients": all_clients,
        "about": about_data,
    })

def get_project(request, id):
    project = Project.objects.filter(pk=id).first()
    about = About.objects.first()
    
    about_data = {
        "instagram": about.instagram,
        "dribble": about.dribble,
        "behance": about.behance,
        "upwork": about.upwork,
        "name": about.name,
        "intro": about.intro
    }
    context = {
        "title": project.title,
        "role": project.role,
        "description": project.description,
        "sections": project.sections,
        "tags": [tag.name for tag in project.tags.all()],
        "components": project.components,
        "banner": project.banner_image,
        "image": project.image,
        "link": project.link,
        "video": project.video,
        "date": project.created_at,
        "proj_type": project.project_type.non_verbose_name,
        "industry": project.industry,

        "about": about_data,
    }
    return render(request, 'project-view.html', context=context)
