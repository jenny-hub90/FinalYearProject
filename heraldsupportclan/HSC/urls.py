from django.urls import path
from django.contrib.auth import views as auth_views


from . import views
from .views import Newsletter, create_post, latest_posts, search_result




urlpatterns = [
   
    path('',views.Home, name='Home'),
    path('team', views.team, name='team'),
    path('Forums',views.Forums, name='Forums'),
    path('detail/<slug>/', views.detail, name='detail'),
    path('posts/<slug>/', views.posts, name='posts'),
    path('login/',views.loginPage, name='login'),
    path('Event',views.Event, name='Event'),
    path('gallery', views.gallery, name='gallery'),
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
     path('Forum_postsapproval',views.Forum_postsapproval , name="Forum_postsapproval"),
    
    path('eventinfo', views.eventinfo, name='eventinfo'),
    path('studentreview', views.studentreview, name='studentreview'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('create_post', create_post, name="create_post"),
    path('latest_posts', latest_posts, name="latest_posts"),
    path('search_result',search_result , name="search_result"),
   
    
]
