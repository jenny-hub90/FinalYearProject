from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class LatestEvents(models.Model):
    
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="HeraldSupportClan")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def _str_(self):
        return self.title + ' | ' + str(self.author)


