from django.db import models

# Create your models here.



class Create_Schools(models.Model):
    school_id=models.CharField(max_length=20)
    school_name=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    est_year=models.CharField(max_length=255)
    school_type=models.CharField(max_length=255)
    lowest_level=models.CharField(max_length=255)
    topest_level=models.CharField(max_length=255)
    cover_pic=models.ImageField(upload_to='images')
    prove_pic=models.ImageField(upload_to='images')
    admin_code=models.CharField(max_length=8)
    teacher_code=models.CharField(max_length=8)
    student_code=models.CharField(max_length=8)


class Joined_Schools(models.Model):
    joined_user_id=models.CharField(max_length=10)
    school_id=models.CharField(max_length=20)
    school_name=models.CharField(max_length=100)
    joined_user_type=models.CharField(max_length=100)
    joined_school_pic=models.ImageField(upload_to='images')  

