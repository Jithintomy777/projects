# from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
# def demo(request):
#     #return HttpResponse('hello world')
#     return render(request,'index0.html')
#
# def about(request):
#     return render(request,'about1.html')
#
# def contact(request):
#     return HttpResponse('I am contact')
# def demo(request):
#     name='india'
#     return render(request,"index0.html",{'obj':name})

# def demo1(request):
#     return render(request,'index1.html')
#
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,'result.html',{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

def demo2(request):
    obj=Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})







