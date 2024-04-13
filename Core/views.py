from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Core.models import Series,Application,Project,Event,Enquiry,Features,Specification,Works,Client
from django.contrib import messages

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    series = Series.objects.all()
    applications = Application.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    enquiries = Enquiry.objects.all()

    context = {
        'page' : 'dashboard',
        'series' : series,
        'applications' : applications,
        'projects' : projects,
        'events' : events,
        'enquiries' : enquiries
    }

    return render(request,'Dashboard/Core/dashboard.html',context)

#----------------------------------- PRODUCTS -----------------------------------#

@login_required
def series(request):
    series = Series.objects.filter(Status=1).order_by('-id')
    context = {
        'page' : 'series',
        'series' : series
    }
    return render(request,'Dashboard/Series/series.html',context)

#----------------------------------- ADD SERIES -----------------------------------#

@login_required
def add_series(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        heading = request.POST.get('heading')
        models = request.POST.get('models')

        image = request.FILES.get('image')
        t_image = request.FILES.get('t-image')

        s_title = request.POST.get('s-title')
        description = request.POST.get('description')

        features = request.POST.getlist('features[]')
        spec_titles = request.POST.getlist('spec-titles[]')
        spec_values = request.POST.getlist('spec-values[]')

        try:
            series = Series.objects.create(
                Title=title,Slug=slug,Image=image,Heading=heading,Models=models,
                Section_Title=s_title,Section_Description=description,Table_Image=t_image
            )

            if features:
                for feature in features:
                    Features.objects.create(Series=series,Title=feature)

            if spec_titles and spec_values:
                for x in range(len(spec_titles)):
                    t = spec_titles[x]
                    v = spec_values[x]
                    Specification.objects.create(Series=series,Title=t,Value=v)

            messages.success(request,'New series added successfully')
            return redirect('series')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-series')
        
    context = {
        'page' : 'series',
    }
    return render(request,'Dashboard/Series/add-series.html',context)

#----------------------------------- EDIT SERIES -----------------------------------#

@login_required
def edit_series(request,slug):
    series = Series.objects.get(Slug=slug)
    features = Features.objects.filter(Series=series)
    specifications = Specification.objects.filter(Series=series)

    if request.method == 'POST':
        if len(request.FILES) > 0:
            series.Image = request.FILES.get('image')

        series.Title = request.POST.get('title')
        series.Slug = request.POST.get('slug')

        try:
            series.save()
            messages.success(request,'Series Details Edited Successfully ... !')
            return redirect('series')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-series',slug=series.Slug)
        
    context = {
        'page' : 'series',
        'series' : series,
        'features' : features,
        'specifications' : specifications
    }
    return render(request,'Dashboard/Series/edit-series.html',context)

#----------------------------------- DELETE SERIES -----------------------------------#

@login_required
def delete_series(request):
    if request.method == 'POST':
        series_id = request.POST.get('series_id')
        series = Series.objects.get(id=series_id)
        series.Status = 0
        series.save()

        return redirect('series')
    
#----------------------------------- APPLICATIONS -----------------------------------#

@login_required
def applcations(request):
    applications = Application.objects.filter(Status=1).order_by('-id')
    context = {
        'page' : 'applications',
        'applications' : applications
    }
    return render(request,'Dashboard/Applications/applications.html',context)

#----------------------------------- ADD APPLICATION -----------------------------------#

@login_required
def add_application(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        image = request.FILES.get('image')
        sub_title = request.POST.get('sub_title')
        description = request.POST.get('description')

        features = request.POST.getlist('features[]')
        works = request.FILES.getlist('works')

        try:
            application = Application.objects.create (
                Title=title,Slug=slug,Image=image,Sub_Title=sub_title,Description=description
            )

            if features:
                for feature in features:
                    Features.objects.create(Application=application,Title=feature)

            if works:
                for work in works:
                    Works.objects.create(Application=application,Image=work)

            messages.success(request,'New Application Added Successfully ... !')
            return redirect('applications')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-application')
        
    context = {
        'page' : 'applications'
    }
    return render(request,'Dashboard/Applications/add-application.html',context)

#----------------------------------- EDIT APPLICATION -----------------------------------#

@login_required
def edit_application(request,slug):
    application = Application.objects.get(Slug=slug)

    context = {
        'page' : 'applications',
        'application' : application
    }
    return render(request,'Dashboard/Applications/edit-application.html',context)

#----------------------------------- DELETE APPLICATION -----------------------------------#

@login_required
def delete_application(request):
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        application = Application.objects.get(id=application_id)
        application.Status = 0
        application.save()
        messages.warning(request,'Application Deleted Successfully ... !')
    return redirect('applications')

#----------------------------------- PROJECTS -----------------------------------#

@login_required
def projects(request):
    projects = Project.objects.all()
    context = {
        'page' : 'projects',
        'projects' : projects
    }
    return render(request,'Dashboard/Projects/projects.html',context)

#----------------------------------- ADD PROJECT -----------------------------------#

@login_required
def add_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        try:
            Project.objects.create(Title=title,Image=image)
            messages.success(request,'Project Created Successfully ... !')
            return redirect('projects-list')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-project')
        
    context = {
        'page' : 'projects'
    }
    return render(request,'Dashboard/Projects/add-project.html',context)

#----------------------------------- EDIT PROJECT -----------------------------------#

@login_required
def edit_project(request,project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        project.Title = request.POST.get('title')
        if len(request.FILES) > 0:
            project.Image = request.FILES.get('image')
        
        project.save()
        return redirect('projects-list')
    context = {
        'page' : 'projects',
        'project' : project
    }
    return render(request,'Dashboard/Projects/edit-project.html',context)

#----------------------------------- DELETE PROJECT -----------------------------------#

@login_required
def delete_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        project = Project.objects.get(id=project_id)
        project.delete()
        messages.warning(request,'project Deleted Successfully ... !')
    return redirect('projects-list')

#----------------------------------- EVENTS -----------------------------------#

@login_required
def events(request):
    events = Event.objects.all()
    context = {
        'page' : 'events',
        'events' : events
    }
    return render(request,'Dashboard/Events/events.html',context)

#----------------------------------- ADD EVENT -----------------------------------#

@login_required
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        date = request.POST.get('date')
        place = request.POST.get('place')

        try:
            Event.objects.create(Title=title,Image=image,Date=date,Place=place)
            messages.success(request,'Event Created Successfully ... !')
            return redirect('events-list')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-event')
        
    context = {
        'page' : 'events'
    }
    return render(request,'Dashboard/Events/add-event.html',context)

#----------------------------------- EDIT EVENT -----------------------------------#

@login_required
def edit_event(request,event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event.Title = request.POST.get('title')
        event.Date = request.POST.get('date')
        event.Place = request.POST.get('place')
        if len(request.FILES) > 0:
            event.Image = request.FILES.get('image')
        
        event.save()
        return redirect('events-list')
    context = {
        'page' : 'events',
        'event' : event
    }
    return render(request,'Dashboard/events/edit-event.html',context)

#----------------------------------- DELETE EVENT -----------------------------------#

@login_required
def delete_event(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = Event.objects.get(id=event_id)
        event.delete()
        messages.warning(request,'event Deleted Successfully ... !')
    return redirect('events-list')

#----------------------------------- CLIENTS -----------------------------------#

@login_required
def clients(request):
    clients = Client.objects.all()
    context = {
        'page' : 'clients',
        'clients' : clients
    }
    return render(request,'Dashboard/Clients/clients.html',context)

#----------------------------------- ADD CLIENTS -----------------------------------#

@login_required
def add_clients(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        for image in images:
            Client.objects.create(Image=image)

    return redirect('clients')

#----------------------------------- DELETE CLIENTS ---------------------------------#

@login_required
def delete_client(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client = Client.objects.get(id=client_id)
        client.delete()
        messages.warning(request,'Client Deleted Successfully ... !')
    return redirect('clients')

#----------------------------------- CONTACT ENQUIRIES ---------------------------------#

@login_required
def enquiries(request,type):
    if type == 'Product':
        enquiries = Enquiry.objects.exclude(Product=None)
        page = 'e-product'
    elif type == 'Service':
        enquiries = Enquiry.objects.exclude(Service=None)
        page = 'e-service'
    else:
        enquiries = Enquiry.objects.filter(Product=None,Service=None)
        page = 'e-contact'

    context = {
        'page' : page,
        'enquiries' : enquiries.order_by('-id'),
        'type' : type
    }
    return render(request,'Dashboard/Enquiries/enquiries.html',context)

#----------------------------------- CONTACT ENQUIRIES ---------------------------------#

@login_required
def delete_enquiry(request):
    if request.method == 'POST':
        enquiry_id = request.POST.get('enquiry_id')
        enquiry = Enquiry.objects.get(id=enquiry_id)
        enquiry.delete()
        messages.warning(request,'Enquiry Deleted Successfully ... !')
    return redirect('enquiries')