from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import Group

# Create your views here.
def login_required(request):
    return render(request, 'users/login_required.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Invalid Login, Please Try Again.')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'users/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)

            group = Group.objects.get(name='users')
            user.groups.add(group)

            if user is not None:
                login(request, user)
                messages.success(request, 'Registration Succesful.')
                return redirect('home')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
            return redirect('register')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})