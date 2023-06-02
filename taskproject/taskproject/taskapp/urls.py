from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about,name='about.html'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail.html'),
    path('thanks/',views.thanks,name='thanks')
]