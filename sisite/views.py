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

@login_required(login_url="/login/")
def api_blogs(request):
    blogs_objs = Blog.objects.all()
   
    price = request.GET.get('price')
    if price :
        blogs_objs = blogs_objs.filter(price__lte=price)  
        
    emenities = request.GET.get('emenities')
    if emenities:
        emenities = emenities.split(',')
        em = []
        for e in emenities:
            try:
                em.append(int(e))
            except Exception as e:
                pass
        # print(em)
        blogs_objs = blogs_objs.filter(emenities__in=em).distinct()
    payload = []
    for blog_obj in blogs_objs:
        result = {}
        result['blog_name'] = blog_obj.blog_name
        result['blog_description'] = blog_obj.blog_description
        result['price'] = blog_obj.price
        payload.append(result)
        
    return JsonResponse(payload, safe=False)
