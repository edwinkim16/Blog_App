from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def home(request):
    emenities = Emenitites.objects.all()
    context = {'emenities': emenities}
    return render(request, 'home.html', context)