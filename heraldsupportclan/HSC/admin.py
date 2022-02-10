from django.contrib import admin
from .models import LatestEvents, Post, slider, review

# Register your models here.

admin.site.register(LatestEvents)
admin.site.register(Post)
admin.site.register(slider)
admin.site.register(review)