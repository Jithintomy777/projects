from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("It is home")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("It is contact")
def detail(request):
    return render(request,'details.html')
def thanks(request):
    return HttpResponse('it is thanks')

