from Core.models import Series,Application

nav_series = Series.objects.filter(Status=1)
nav_applications = Application.objects.filter(Status=1)

def context(request):
    context = {
        'nav_series' : nav_series,
        'nav_applications' : nav_applications
    }
    return context