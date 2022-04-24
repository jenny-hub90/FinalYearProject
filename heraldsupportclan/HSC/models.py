from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from pytz import timezone
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from django.urls import reverse


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

class review(models.Model):
    studentimage = models.ImageField(max_length=800,upload_to="students/", blank=False)
    studentreview = models.TextField(max_length=800, blank=False)
    studentname = models.CharField(max_length=200, blank=False)
    
class Toppost(models.Model):
    newstitle = models.CharField(max_length=255, blank=False)
    newsimage = models.ImageField(max_length=800,upload_to="eventstudentsreview/", blank=False)
    newsdesc = models.TextField(max_length=800, blank=False)


class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to="slider/", blank=False)



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

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = HTMLField()
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(size=[50,80],quality=100, upload_to="authors", default=None, null=True, blank=True)
    
    def __str__(self):
        return self.fullname
    
    @property
    def num_posts(self):
        return ForumPost.objects.filter(user=self).count()


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True,blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    
    def get_url(self):
        return reverse("posts", kwargs={
            "slug": self.slug
        })
    
    @property
    def num_posts(self):
        return ForumPost.objects.filter(categories=self).count()

    @property
    def last_post(self):
        return ForumPost.objects.filter(categories=self).latest("date")

class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.content[:100]
    
    class Meta:
        verbose_name_plural = "replies"


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply,blank=True)

    def __str__(self):
        return self.content[:100]

    
class ForumPost(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation'
    )
    tags = TaggableManager()
    comments = models.ManyToManyField(Comment, blank=True)
    closed = models.BooleanField(default=False)
    state = models.CharField(max_length=40, default="zero")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ForumPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug
        })

    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest("date")


class Gallery(models.Model):
    gallerytitle = models.CharField(max_length=255, blank=False)
    galleryimage = models.ImageField(max_length=800,upload_to="galleryimage/", blank=False)

class EventGalleryCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True,blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "eventCategory"
    def __str__(self):
        return self.title

    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(EventGalleryCategory, self).save(*args, **kwargs)

class EventGalleryPictures(models.Model):
    eventCategory = models.ManyToManyField(EventGalleryCategory)
    eventimage = models.ImageField(max_length=800,upload_to="eventgallery/", blank=False)

 
class Notify(models.Model):
    notify_detail= models.TextField()
    ready_by_User= models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    ready_by_Author= models.ForeignKey(Author, on_delete= models.CASCADE, null=True, blank=True)
   
    def __str__(self):
        return str(self.notify_detail)

# Mark Read notifications By User
class NotifUserStatus(models.Model):
    notif= models.ForeignKey(Notify, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    