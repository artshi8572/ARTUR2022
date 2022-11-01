from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'about.html',{'daff':"HELLO"},)

def home(request):
    return HttpResponse("ЭТО МОЙ САЙТ")