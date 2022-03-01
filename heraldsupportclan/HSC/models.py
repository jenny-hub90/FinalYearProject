from distutils.command.upload import upload
from email.mime import image

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, date
# Create your models here.
class LatestEvents(models.Model):
    
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="HeraldSupportClan")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Toppost(models.Model):
    newstitle = models.CharField(max_length=255, blank=False)
    newsimage = models.ImageField(max_length=800,upload_to="eventstudentsreview/", blank=False)
    newsdesc = models.TextField(max_length=800, blank=False)


class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to="slider/", blank=False)

class review(models.Model):
    studentimage = models.ImageField(max_length=800,upload_to="students/", blank=False)
    studentreview = models.TextField(max_length=800, blank=False)
    studentname = models.CharField(max_length=200, blank=False)

class Eventslider(models.Model):
    eventimg = models.ImageField(max_length=800,upload_to="events/", blank=False)

class Eventabout(models.Model):
    aboutimage = models.ImageField(max_length=800,upload_to="eventsabout/", blank=False)
    aboutdesc = models.TextField(max_length=1000, blank=False)
    moredesc = models.TextField(max_length=500, blank=False) 
    
class EventReview(models.Model):
    studentimage = models.ImageField(max_length=800,upload_to="eventstudentsreview/", blank=False)
    studentreview = models.TextField(max_length=800, blank=False)
    studentname = models.CharField(max_length=200, blank=False)
    studentcourse = models.CharField(max_length=200, blank=False)
     
