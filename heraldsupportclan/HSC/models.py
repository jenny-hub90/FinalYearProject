from distutils.command.upload import upload
from email.mime import image
from statistics import mode
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

class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to="slider/", blank=False)

class review(models.Model):
    studentimage = models.ImageField(max_length=800,upload_to="students/", blank=False)
    studentreview = models.TextField(max_length=800, blank=False)
    studentname = models.CharField(max_length=200, blank=False)

class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
    def get_responses(self):
        return self.responses.filter(parent= None)

class Respose(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE, related_name='responses')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_responses(self):
        return Respose.objects.filter(parent=self)

class Eventslider(models.Model):
    eventimg = models.ImageField(max_length=800,upload_to="events/", blank=False)
     
