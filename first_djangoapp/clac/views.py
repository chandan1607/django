from os import name
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'chandan'})

def add(request):
    var1 = int(request.POST['num1'])
    var2 = int(request.POST['num2'])
    res = var2 + var1
    return render(request,'result.html',{'result': res})