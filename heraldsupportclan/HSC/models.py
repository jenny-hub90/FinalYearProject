from distutils.command.upload import upload
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

    def _str_(self):
        return self.title + ' | ' + str(self.author)


