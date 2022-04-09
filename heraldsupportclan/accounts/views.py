from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required







def registerPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            # user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + new_user)

            return redirect('update_profile')
    
    context = {'form':form}
    return render(request,'accounts/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
        # username = request.POST.get('username')
        # password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('update_profile')

    context ={}
    return render(request,'accounts/login.html', context)




@login_required(login_url='register')
def logoutUser(request):
	logout(request)
	return redirect('Home')




class UserRegisterView(generic.CreateView):
     form_class = SignUpForm
     template_name = 'registration/register.html'
     success_url = reverse_lazy('login')

