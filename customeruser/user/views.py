from atexit import register
from django.http import HttpResponse

from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from user.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'userhome.html')


def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = AuthenticationForm()
        if request.method =='POST':
            form = AuthenticationForm(request, data=request.POST)
            print(form)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                print(username,password,'*'*58)
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')

        context = {
            'form':form,
        }
        return render(request,'login.html',context)

def userCreation(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {
            'forms':form,
        }
        return render(request,'register.html',context)

# logout view

def logoutView(request):
    logout(request)
    return redirect('login')
