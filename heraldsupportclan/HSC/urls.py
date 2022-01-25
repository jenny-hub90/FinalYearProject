from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.Home, name='Home'),
    path('F',views.F, name='F'),
    path('Login',views.Login, name='Login'),
    path('Event',views.Event, name='Event'),
    path('Newsletter',views.Newsletter, name='Newsletter'),
  
]
