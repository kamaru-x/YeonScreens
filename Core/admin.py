from django.contrib import admin
from Core.models import Series,Features,Specification,Application,Works,Project

# Register your models here.

@admin.register(Series)
class SeriesModelAdmin(admin.ModelAdmin):
    list_display = ['Title','Slug']

@admin.register(Features)
class FeaturesModelAdmin(admin.ModelAdmin):
    list_display = ['Series','Title']

@admin.register(Specification)
class SpecificationModelAdmin(admin.ModelAdmin):
    list_display = ['Series','Title','Value']

@admin.register(Application)
class ApplicationModelAdmin(admin.ModelAdmin):
    list_display = ['Title','Slug']

@admin.register(Works)
class WorksModelAdmin(admin.ModelAdmin):
    list_display = ['Application']

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['Title']