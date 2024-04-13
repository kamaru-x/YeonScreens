from django.shortcuts import render
from Core.models import Series,Features,Specification,Application,Works,Project,Event

# Create your views here.

def home(request):
    applications = Application.objects.all()
    projects = Project.objects.all().order_by('-id')[:3]
    context = {
        'page' : 'home',
        'applications' : applications,
        'projects' : projects
    }
    return render(request,'Web/index.html',context)

def about(request):
    context = {
        'page' : 'about'
    }
    return render(request,'Web/about.html',context)

def contact(request):
    context = {
        'page' : 'contact'
    }
    return render(request,'Web/contact.html',context)

def application(request,slug):
    application = Application.objects.get(Slug=slug)
    features = Features.objects.filter(Application=application)
    works = Works.objects.filter(Application=application)
    context = {
        'page' : 'application',
        'application' : application,
        'features' : features,
        'works' : works
    }
    return render(request,'Web/application.html',context)

def events(request):
    events = Event.objects.all()
    context = {
        'page' : 'events',
        'events' : events
    }
    return render(request,'Web/events.html',context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'page' : 'projects',
        'projects' : projects
    }
    return render(request,'Web/projects.html',context)

def project_details(request,prj):
    context = {
        'page' : 'projects'
    }
    return render(request,'Web/project-details.html',context)

def product_details(request,slug):
    series = Series.objects.get(Slug=slug)
    features = Features.objects.filter(Series=series)
    specifications = Specification.objects.filter(Series=series)
    context = {
        'page' : 'products',
        'series' : series,
        'features' : features,
        'specifications' : specifications
    }
    return render(request,'Web/product-details.html',context)