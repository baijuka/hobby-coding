from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Project

# Create your views here.

def projects(request):

    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):

    projectObject = Project.objects.get(id=pk)
    tags = projectObject.tags.all()
    reviews = projectObject.review_set.all()
    context = {'project':projectObject, 'tags':tags, 'reviews':reviews}
    return render(request, 'projects/single-project.html', context)