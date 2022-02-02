from django.shortcuts import render
from .models import LatestEvents, Post
from django.views.generic import ListView, DetailView


# Create your views here.
def Home(request):
   secs = LatestEvents.objects.all()
   
   return render(request,'Home.html', {'secs': secs})

def F(request):
    return render(request,'F.html')

def Login(request):
    return render(request,'Login.html')

def Event(request):
    return render(request,'Event.html')

#def Newsletter(request):
    #return render(request,'Newsletter.html', {})
class Newsletter(ListView):
    model = Post
    template_name = 'Newsletter.html'

# class Newsletter(DetailView):
#     model = Post
#     template_name = 'Newsletter.html'


