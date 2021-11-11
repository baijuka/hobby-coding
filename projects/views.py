from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.

projectlist = [
    {'id':'1',
     'title':'Ecommerce Website',
     'description':'Fully functional ecommerce website'
     },
    {'id':'2',
     'title':'Hotel Management System',
     'description':'Hotel Management System Development for Holiday Inn, London'
     },
    {'id':'3',
     'title':'Patient Appointment Booking App',
     'description':'Patient appointment booking site for a Glan-Usk Surgery'
     },
    {'id':'4',
     'title':'Online Ticket Booking System',
     'description':'Ticket booking site development'
     }
    ]


def projects(request):

    context = {'projects':projectlist}
    return render(request, 'projects/projects.html', context)


def project(request, pk):

    projectlist = [
        {'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website'
        },
        {'id':'2',
        'title':'Hotel Management System',
        'description':'Hotel Management System Development for Holiday Inn, London'
        },
        {'id':'3',
        'title':'Patient Appointment Booking App',
        'description':'Patient appointment booking site for a Glan-Usk Surgery'
        },
        {'id':'4',
        'title':'Online Ticket Booking System',
        'description':'Ticket booking site development'
        }]
    
    projectObject = None

    for i in projectlist:
        if i['id']==str(pk):
            projectObject = i
    return render(request, 'projects/single-project.html', {'project':projectObject})