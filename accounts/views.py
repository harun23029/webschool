from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import   Create_Schools,Joined_Schools
import secrets 
import string

# Create your views here.
def signup(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect(signup)
        else:
            user = User.objects.create_user(email=email,username=username, password=password,first_name=firstname,last_name=lastname)
            user.save()
            return redirect('/')
    elif request.method == 'GET':
        return render(request,'signup.html')

def signin(request): 
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or password is incorrect')
            return redirect(signin)

    elif request.method == 'GET':
        return render(request,'signin.html')

def signout(request):
    auth.logout(request)
    return redirect('/')

def create_join(request):
    return render(request,'create_join.html',{'join_type':'create'})


def  create_school(request):
    if request.method=='POST':
        school_name=request.POST['school_name']
        address=request.POST['address']
        est_year=request.POST['est_year']
        school_type=request.POST['school_type']
        lowest_level=request.POST['lowest_level']
        topest_level=request.POST['topest_level']
        cover_pic=request.POST['cover_pic']
        prove_pic=request.POST['prove_pic']
        N=7
        admin_code = ''.join(secrets.choice(string.ascii_uppercase+string.digits) 
        for i in range(N))
        admin_code='A'+admin_code
        teacher_code = ''.join(secrets.choice(string.ascii_uppercase+string.digits) 
        for i in range(N))
        teacher_code='T'+teacher_code
        student_code=''.join(secrets.choice(string.ascii_uppercase+string.digits) 
        for i in range(N))
        student_code='S'+student_code
        M=20
        school_id=''.join(secrets.choice(string.ascii_uppercase+string.digits) 
        for i in range(M))
        if Create_Schools.objects.filter(school_name=school_name,address=address).exists():
            return render(request,'create_join.html',{'msg':'1'})
        else:
            school=Create_Schools(school_id=school_id,school_name=school_name,address=address,est_year=est_year,school_type=school_type,lowest_level=lowest_level,topest_level=topest_level,cover_pic=cover_pic,prove_pic=prove_pic,admin_code=admin_code,teacher_code=teacher_code,student_code=student_code)
            school.save()
            return render(request,'create_join.html',{'join_type':'join','admin_code':admin_code,'teacher_code':teacher_code,'student_code':student_code})

def join_user(request):
    if request.method=='POST':
        user_type=request.POST['user_type']
        join_code=request.POST['join_code']
        joined_user_id=request.user.get_username()
        joined_all_schools=Joined_Schools.objects.filter(joined_user_id=joined_user_id).all()
        
        if user_type=='Adminstrator':
            if   Create_Schools.objects.filter(admin_code=join_code).exists():
                school=Create_Schools.objects.all().filter(admin_code=join_code)
                school_id=school[0].school_id
                school_name=school[0].school_name
                cover_pic=school[0].cover_pic
                
                if Joined_Schools.objects.filter(joined_user_id=joined_user_id,school_id=school_id).exists():

                    return render(request,'schools.html',{'joined_user':joined_all_schools})
                else:
                    joined_school=Joined_Schools(joined_user_id=joined_user_id,school_id=school_id,joined_user_type="Adminstrator",school_name=school_name,joined_school_pic=cover_pic)
                    joined_school.save()
                    return render(request,'schools.html',{'joined_user':joined_all_schools})
            else:
                return render(request,'create_join.html',{'join_type':'join_old'})
        elif user_type=='Teacher':
            if   Create_Schools.objects.filter(teacher_code=join_code).exists():
                school=Create_Schools.objects.all().filter(teacher_code=join_code)
                school_id=school[0].school_id
                school_name=school[0].school_name
                cover_pic=school[0].cover_pic

                if Joined_Schools.objects.filter(joined_user_id=joined_user_id,school_id=school_id).exists():

                    return render(request,'schools.html',{'joined_user':joined_all_schools})
                else:
                    joined_school=Joined_Schools(joined_user_id=joined_user_id,school_id=school_id,joined_user_type="Teacher",school_name=school_name,joined_school_pic=cover_pic)
                    joined_school.save()
                    return render(request,'schools.html',{'joined_user':joined_all_schools})
            else:
                return render(request,'create_join.html',{'join_type':'join_old'})
        else:
             if  Create_Schools.objects.filter(student_code=join_code).exists():
                school=Create_Schools.objects.all().filter(student_code=join_code)
                school_id=school[0].school_id
                school_name=school[0].school_name
                cover_pic=school[0].cover_pic

                if Joined_Schools.objects.filter(joined_user_id=joined_user_id,school_id=school_id).exists():
                    return render(request,'schools.html',{'joined_user':joined_all_schools})
                else:
                    joined_school=Joined_Schools(joined_user_id=joined_user_id,school_id=school_id,joined_user_type="Student",school_name=school_name,joined_school_pic=cover_pic)
                    joined_school.save()
                    return render(request,'schools.html',{'joined_user':joined_all_schools})
             else:
                return render(request,'create_join.html',{'join_type':'join_old'})


