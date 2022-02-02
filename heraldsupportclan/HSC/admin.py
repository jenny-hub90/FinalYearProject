from django.contrib import admin
from .models import LatestEvents, Post

# Register your models here.

admin.site.register(LatestEvents)
admin.site.register(Post)
