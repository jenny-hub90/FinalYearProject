from django.shortcuts import render
from .models import EventReview, LatestEvents, Post, slider, review,  Eventslider, Eventabout
from django.views.generic import ListView




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
    return render(request,'Forums.html')

def detail(request):
    return render(request,'detail.html')

def posts(request):
    return render(request,'posts.html')



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



