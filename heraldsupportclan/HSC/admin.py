from django.contrib import admin
from .models import LatestEvents, Post, slider, review,Question, Respose, Eventslider, Eventabout, EventReview, Toppost

# Register your models here.

admin.site.register(LatestEvents)
admin.site.register(Post)
admin.site.register(slider)
admin.site.register(review)
admin.site.register(Question)
admin.site.register(Respose)
admin.site.register(Eventslider)
admin.site.register(Eventabout)
admin.site.register(EventReview)
admin.site.register(Toppost)