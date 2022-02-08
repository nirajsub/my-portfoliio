from django.contrib import admin
from .models import*

admin.site.register(
    [Planguage, Dtool, skills, Project, ProjectLanguage, ProjectTool, Contact, Framework, DataBase, ProjectFramework, ProjectDatabase]
)