from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def registerPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)

            return redirect('login')
    
    context = {'form':form}
    return render(request,'accounts/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')

    context ={}
    return render(request,'accounts/login.html', context)
 

def logoutUser(request):
	logout(request)
	return redirect('Home')

class UserRegisterView(generic.CreateView):
     form_class = SignUpForm
     template_name = 'registration/register.html'
     success_url = reverse_lazy('login')
