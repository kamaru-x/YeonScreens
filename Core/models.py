from django.db import models
from U_Auth.models import User

# Create your models here.

######################################################################

class Series(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    
    Title = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='Series',null=True)
    Slug = models.CharField(max_length=50,null=True,unique=True)

    Heading = models.CharField(max_length=100,null=True)
    Models = models.CharField(max_length=100,null=True)

    Section_Title = models.CharField(max_length=100,null=True)
    Section_Description = models.TextField(null=True)

    Table_Image = models.ImageField(upload_to='Series',null=True)

    def __str__(self):
        return self.Title

######################################################################

class Specification(models.Model):
    Series = models.ForeignKey(Series,on_delete=models.CASCADE)

    Title = models.CharField(max_length=50)
    Value = models.CharField(max_length=50)

    def __str__(self):
        return self.Title
    
######################################################################

class Application(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)

    Title = models.CharField(max_length=225)
    Slug = models.CharField(max_length=225,unique=True,null=True)
    Image = models.ImageField(upload_to='Applications',null=True)
    Sub_Title = models.CharField(max_length=100,null=True)
    Description = models.TextField(null=True)

    def __str__(self):
        return self.Title

######################################################################

class Features(models.Model):
    Series = models.ForeignKey(Series,on_delete=models.CASCADE,null=True)
    Application = models.ForeignKey(Application,on_delete=models.CASCADE,null=True)
    Title = models.CharField(max_length=100)

    def __str__(self):
        return self.Title
    
######################################################################

class Works(models.Model):
    Application = models.ForeignKey(Application,on_delete=models.CASCADE,null=True)
    Image = models.ImageField(upload_to='Works',null=True)
    
######################################################################

class Project(models.Model):
    Date = models.DateField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    Title = models.CharField(max_length=225)
    Image = models.ImageField(upload_to='Projects',null=True)

    def __str__(self):
        return self.Title

######################################################################

class Event(models.Model):
    Title = models.CharField(max_length=225)
    Image = models.ImageField(upload_to='Events',null=True)
    Date = models.DateField(null=True)
    Place = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.Title

######################################################################

class Enquiry(models.Model):
    Name = models.CharField(max_length=100)