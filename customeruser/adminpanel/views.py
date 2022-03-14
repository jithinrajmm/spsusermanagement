
from multiprocessing import context
import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from adminpanel.forms import CustomUserCreationFormAdmin,AdminForm
from django.contrib import messages
from adminpanel.models import Admin
from django.db.models import Q

# Create your views here.

def AdminHome(request):
    if 'id' in request.session:
        users = User.objects.all()
        user_count = users.count()
        deactive_count = User.objects.filter(is_active=False).count()
        active_count = User.objects.filter(is_active=True).count()
        form = CustomUserCreationFormAdmin()
        if request.GET.get('q'):
            q = request.GET.get('q')
            users = User.objects.filter(Q(username__icontains = q)| Q(email__icontains=q))
        context = {
            'users':users,
            'user_count': user_count,
            'deactive_count':deactive_count,
            'active_count': active_count,
            'formsaadmin': form,
        }
        return render(request, 'home.html',context)
    else:
        return redirect('adminLogin')

def details(request,pk):
    user = User.objects.get(id=pk)
    print(user.username, user.email)
    context = {
        'name': user.username,
        'email': user.email,
    }
    return JsonResponse(context)


def update_view(request,pk):

    if request.method == "POST":

        user = User.objects.get(id=pk)

        name = request.POST.get('user_name')
        email = request.POST.get('email')
        user.username = name
        user.email = email
        user.save()
        print(user.username,user.email)

        context = {
            'name': user.username,
            'email': user.email,
            'id':user.id,
        }
        return JsonResponse(context)

    user = User.objects.get(id=pk)
    context = {
        'name': user.username,
        'email': user.email,
        'id': user.id,
    }
    return JsonResponse(context)

def user_activation(request):

    id = request.GET.get('id')
    user = User.objects.get(id=id)
    if user.is_active:
        user.is_active = False
        user.save()

    else:
        user.is_active = True
        user.save()
    print(user.is_active)
    return JsonResponse({'success': user.is_active,'id': user.id})


def adminLogin(request):
    if 'id' in request.session:
        return redirect('adminhome')
    else:
        form = AdminForm(request.POST or None)
        if request.method == 'POST':
            user_name = request.POST.get('admin_name')
            password1 = request.POST.get('password')
            print(user_name)
            print(password1)
            if Admin.objects.filter(admin_name=user_name,password=password1).exists():
                user = Admin.objects.get(admin_name=user_name,password=password1)
                authenticated = user.admin_authenticate(user_name,password1)
                if authenticated:
                    request.session['id']=user.id
                    print(request.session.get('id'))
                    return redirect('adminhome')
            else:
                messages.error(request, 'Not valid credentials')

        context = {
            'form':form
        }

        return render(request,'adminlogin.html',context)

def logout_admin(request):

    if 'id' in request.session:
        request.session.flush()
        return redirect('adminLogin')