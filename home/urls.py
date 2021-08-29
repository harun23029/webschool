from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('savecontact',views.savecontact,name='index'),
    path('home',views.home,name='home'),
    path('gotoschool',views.gotoschool,name='gotoschool'),
]