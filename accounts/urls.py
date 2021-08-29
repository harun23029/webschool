from django.urls import path
from . import views

urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('create_join',views.create_join,name='create_join'),
    path('signout',views.signout,name='signout'),
    path('create_school',views.create_school,name='create_school'),
    path('join_user',views.join_user,name="join_user")
]