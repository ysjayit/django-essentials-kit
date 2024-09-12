from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from .models import UserProfile


@login_required(login_url='login')
def index(request):
    profile = request.user.userprofile
    return render(request, 'dashboard.html', {'profile': profile})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def user_list(request):
    return render(request, 'users.html')


@unauthenticated_user
def user_register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # add to user group
            group = Group.objects.get(name='users')
            user.groups.add(group)

            # add to user profile
            UserProfile.objects.create(
                user=user,
            )

            messages.success(request, 'Account created for ' + username)
            return redirect('login')
        else:
            messages.error(request, 'Error occured during registraion.')

    return render(request, 'register.html', {'form': form})


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User not exist')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Email or password incorrect.")
        else:
            messages.error(request, "Email or password not provided.")

    return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def user_settings(request):
    profile = request.user.userprofile
    form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'settings.html', {'form': form})
