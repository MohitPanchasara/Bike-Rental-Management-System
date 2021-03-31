from django.shortcuts import render, redirect
from .models import userInfo, User, Station, Bike
from .forms import userForm, userInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .filters import bike_filter

# Create your views here.


def home(request):
    stations = Station.objects.all()
    bikes = Bike.objects.all()
    bikes_filter = bike_filter(request.GET, queryset=bikes)
    context = {'stations': stations, 'bikes': bikes, 'filter': bikes_filter}
    return render(request, 'home.html', context)


def register_user(request):

    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = userInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            return redirect('home')

        else:
            context = {'user_form.errors': user_form.errors,
                       'user_info_form.errors': user_info_form.errors}
            return render(request, 'user/register.html', context)
    else:

        user_form = userForm()
        user_info_form = userInfoForm()

        context = {'user_form': user_form,
                   'user_info_form': user_info_form}

        return render(request, 'user/register.html', context)


def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username or password is not valid!')
            return redirect('login_user')

    return render(request, 'user/login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')
