from django.contrib import admin
from .models import  NotifUserStatus, Notify,EventGalleryCategory, EventGalleryPictures, LatestEvents, Post, slider,  Eventslider, Eventabout, EventReview, Toppost, Category, Author, ForumPost, Comment, Reply, Gallery,review

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
admin.site.register(Notify)
admin.site.register(NotifUserStatus)


# class NotifyAdmin(admin.ModelAdmin):
#     list_display = (' notify_detail', 'ready_by_User','ready_by_Author')

