from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import Joined_Schools,Create_Schools
from django.contrib.auth.models import User,auth
from .models import Contacts

# Create your views here.
def index(request):
    return render(request,'index.html')

def gotoschool(request):
    joined_user_id=request.user.get_username()
    joined_all_schools=Joined_Schools.objects.filter(joined_user_id=joined_user_id).all()
    return render(request,'schools.html',{'joined_user':joined_all_schools})

def home(request):
    return render(request,'index.html')

def savecontact(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    message=request.POST['message']

    contacts=Contacts(name=name,email=email,phone=phone,message=message)
    contacts.save()

    return redirect('/')

