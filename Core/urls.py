from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('series/',views.series,name='series'),
    path('series/add/',views.add_series,name='add-series'),
    path('series/edit/<str:slug>/',views.edit_series,name='edit-series'),
    path('series/delete/',views.delete_series,name='delete-series'),

    path('applications/',views.applcations,name='applications'),
    path('application/add/',views.add_application,name='add-application'),
    path('application/edit/<str:slug>/',views.edit_application,name='edit-application'),
    path('application/delete/',views.delete_application,name='delete-application'),

    path('projects/',views.projects,name='projects-list'),
    path('project/add/',views.add_project,name='add-project'),
    path('project/edit/<str:project_id>/',views.edit_project,name='edit-project'),
    path('project/delete/',views.delete_project,name='delete-project'),

    path('events/',views.events,name='events-list'),
    path('event/add/',views.add_event,name='add-event'),
    path('event/edit/<str:event_id>/',views.edit_event,name='edit-event'),
    path('event/delete/',views.delete_event,name='delete-event'),
]