from django.shortcuts import render
from .models import Person, Project, Tag, Information, Skill

# Create your views here.
def main(response):
    person = Person.objects.get(id='01')
    infomation = Information.objects.get(id='1')
    projects = Project.objects.all().order_by('id').values()

    context = {'ps': person, 'infomation': infomation, 'proj': projects}
    return render(response, "main.html", context)

def profile(response):
    person = Person.objects.get(id='01')
    context = {'ps': person}
    return render(response, "dashboard/dashboard.html", context)

def biography(response):
    infomation = Information.objects.get(id='1')
    context = {'infomation': infomation}
    return render(response, "dashboard/biography.html", context)

def skills(response):
    skills = Skill.objects.all()
    tags = Tag.objects.all()
    context = {'skills': skills}
    return render(response, "dashboard/skills.html", context)

def projects(response):
    person = Person.objects.get(id='01')
    projects = Project.objects.all()
    context = {'proj': projects, 'ps': person}

    return render(response, "dashboard/projects.html", context)

def contact(response):
    person = Person.objects.get(id='01')
    context = {'ps': person}
    return render(response, "dashboard/contact.html", context)

def tags(response):
    tag = Person.objects.get(id='01')
    context = {'ps': person}
    return render(response, "dashboard/contact.html", context)
