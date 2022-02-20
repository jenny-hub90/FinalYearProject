from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from .models import LatestEvents, Post, slider, review, Question
from django.views.generic import ListView, DetailView
from .forms import NewQuestionForm, NewResoponseForm


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
   return render(request,'Home.html', {'secs': secs})

def newQuestionPage(request):
    form = NewQuestionForm()
    
    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
        except Exception as e:
            print(e)

    context={'form': form}
    return render(request, 'new-question.html', context)

def F(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request,'F.html', context)


def questionPage(request, id):
    response_form = NewResoponseForm()

    if request.method == 'POST':
        try:
            response_form = NewResoponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+ str(id)+ '#'+ str(response.id))
        except Exception as e:
            print(e)
            raise


    question = Question.objects.get(id=id)
    context ={
        'question': question,
        'response_form':response_form
    }
    return render(request, 'question.html', context)


def Event(request):
    return render(request,'Event.html')


def changepassword(request):
    return render(request, 'change-password.html')

def eventinfo(request):
    sliderdata = slider.objects.all()
    return render(request,'eventinfo.html',{'sliderdata':sliderdata})

def studentreview(request):
    students= review.objects.all()
    return render(request, 'studentreview.html',{'students': students})
#def Newsletter(request):
    #return render(request,'Newsletter.html', {})
class Newsletter(ListView):
    model = Post
    template_name = 'Newsletter.html'
    ordering = ['-post_date']

# class Newsletter(DetailView):
#     model = Post
#     template_name = 'Newsletter.html'


