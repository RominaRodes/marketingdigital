from django.shortcuts import render
from django.utils.translation import gettext as _

def landing_view(request):
    
    return render(request, 'landing/index2.html')


def landing2_view(request):
    
    return render(request,'landing/index.html')

def nosotros_view(request):
    
    return render(request, 'landing/index3.html')

def coming_soon(request):
    return render(request, 'landing/coming_soon.html')

def final(request):
    return render(request, 'landing/final.html')