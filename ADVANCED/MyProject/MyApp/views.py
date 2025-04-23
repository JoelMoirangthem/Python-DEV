from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def loginPage(request):
    page = 'Login'
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request,"User Does Not Exist")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context = {'page' : page}
    return render(request,'login.html',context)
# def logoutPage(request):
def logoutuser(request):
    logout(request)
    return redirect('login')

def Registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"error in registration")
    return render(request,'login.html',{"form":form})
def home(request):
    page = 'home'
    return render(request,'home.html',{'page':page})
def about(request): 
    page = 'Login'
    return render(request,'about.html',{"page":page})