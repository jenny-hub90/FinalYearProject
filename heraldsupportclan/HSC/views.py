from django.shortcuts import render, get_object_or_404
from .models import EventReview, LatestEvents, Post, slider, review,  Eventslider, Eventabout, Category, ForumPost, Author
from django.views.generic import ListView
from .utils import update_views




# Create your views here.

def registerPage(request):
    context ={}
    return render(request,'registration/register.html', context)

def loginPage(request):
    context ={}
    return render(request,'registration/login.html', context)
    
def ForgotPassword(request):
    return render(request, 'ForgotPassword.html')

def Home(request):
   secs = LatestEvents.objects.all()
   students= review.objects.all()
   return render(request,'Home.html', {
       'secs': secs,
       'students':students,
   })

def Forums(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request,'Forums.html',context)

def detail(request, slug):
    post = get_object_or_404(ForumPost, slug=slug)
    context={
        "post":post
    }
    update_views(request, post)

    return render(request,'detail.html', context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = ForumPost.objects.filter(approved=True, categories=category)

    context = {
        "posts":posts,
        "forum": category,
    }
    return render(request,'posts.html',context)



def Event(request):
    eventslider= Eventslider.objects.all()
    eventabout= Eventabout.objects.all()
    eventreview = EventReview.objects.all()
    return render(request,'Event.html',{
        'eventslider':eventslider,
        'eventabout': eventabout,
        'eventreview': eventreview,
        })


def changepassword(request):
    return render(request, 'change-password.html')

def eventinfo(request):
    sliderdata = slider.objects.all()
    return render(request,'eventinfo.html',{'sliderdata':sliderdata})

def studentreview(request):
    students= review.objects.all()
    return render(request, 'studentreview.html',{'students': students})

class Newsletter(ListView):
    model = Post
    template_name = 'Newsletter.html'
    ordering = ['-post_date']



