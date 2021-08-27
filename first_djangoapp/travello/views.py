from travello.models import destination
from django.shortcuts import render

# Create your views here.

def index(request):
    
    dests = destination.objects.all()

    return render(request,'index.html',{'dests':dests})

def contact(request):
    return render(request,'contact.html')

def des(request):
    return render(request,'destinations.html')