from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import PhotoUploadForm


# Create your views here.pyth

def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form1': form}
    return render(request, 'registration/register.html', context)

def logOutDash(request):
    logout(request)
    return render(request,'registration/logged_out.html')

@login_required(login_url='login')
def deletePhoto(request):
    context = {}
    return render(request,'delete.html',context)

def home(request):
    photo = PhotoFeed.objects.all()
    photos = {'Photos':photo}
    return render(request, 'home.html',photos)

@login_required(login_url='login')
def dashboard(request):
    photo = PhotoFeed.objects.all()
    photos = {'PNG':photo}
    return render(request, 'dashboard.html',photos)

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'changepw': form}
    return render(request, 'users.html', context)

@login_required(login_url='login')
def upload_photo(request):
    form = PhotoUploadForm()
    context = {'photo':form}
    if request.method == 'POST':
        if form.is_valid():
            form = PhotoUploadForm()
            form.save()
            return redirect('dashboard')
    return render(request, 'photos.html',context)