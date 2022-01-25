from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html')

def F(request):
    return render(request,'F.html')

def Login(request):
    return render(request,'Login.html')

def Event(request):
    return render(request,'Event.html')

def Newsletter(request):
    return render(request,'Newsletter.html')


