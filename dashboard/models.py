from django.db import models

# Create your models here.
 
class Person(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default="None")
    surname = models.CharField(max_length=50)
    profile_caption = models.CharField(max_length=50, default="None")
    email = models.CharField(max_length=100)
    cell = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    
    image = models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='posters')
    
    link = models.CharField(max_length=1000, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title

class Information(models.Model):
    information = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='info')
    styleId = models.TextField(max_length=10)

    def __str__(self):
        return self.information

class Skill(models.Model):
    skill = models.TextField(max_length=50)
    rate = models.IntegerField()

    def __str__(self):
        return self.skill
