from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import Newsletter

urlpatterns = [
   
    path('',views.Home, name='Home'),
    path('F',views.F, name='F'),
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('Event',views.Event, name='Event'),
    path('Newsletter', Newsletter.as_view(), name="Newsletter"),
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), 
    name="password_reset_complete"),
    
    path('eventinfo', views.eventinfo, name='eventinfo'),
    path('studentreview', views.studentreview, name='studentreview'),
]
