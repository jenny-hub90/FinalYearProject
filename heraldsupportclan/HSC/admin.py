from django.contrib import admin
from .models import  EventGalleryCategory, EventGalleryPictures, LatestEvents, Post, slider, review, Eventslider, Eventabout, EventReview, Toppost, Category, Author, ForumPost, Comment, Reply, Gallery

# Register your models here.

admin.site.register(LatestEvents)
admin.site.register(Post)
admin.site.register(slider)
admin.site.register(review)
admin.site.register(Eventslider)
admin.site.register(Eventabout)
admin.site.register(EventReview)
admin.site.register(Toppost)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(ForumPost)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Gallery)
admin.site.register(EventGalleryCategory)
admin.site.register(EventGalleryPictures)
