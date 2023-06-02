from django.urls import path,include
from . import views

urlpatterns = [

    #path('',views.demo,name='demo')
    # path('about/',views.about,name='about1.html'),
    # path('contact/',views.contact,name='contact')
    # path('',views.demo1,name='demo1'),
    # path('add/',views.addition,name='addition')
    path('',views.demo2,name='demo2')
    ]