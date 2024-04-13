from django.urls import path
from WebPage import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('application/<str:slug>/',views.application,name='application'),
    path('events/',views.events,name='events'),
    path('projects/',views.projects,name='projects'),
    path('project/details/<str:prj>/',views.project_details,name='project-details'),
    path('product/<str:slug>/',views.product_details,name='product-details'),
]