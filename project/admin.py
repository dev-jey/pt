from django.contrib import admin

from project.models import Project, About, Skill, ProjectType, Image, Section, ProjectTag, Component,MyClient

admin.site.register(Project)
admin.site.register(ProjectType)
admin.site.register(ProjectTag)
admin.site.register(Skill)
admin.site.register(About)
admin.site.register(Image)
admin.site.register(Section)
admin.site.register(Component)
admin.site.register(MyClient)