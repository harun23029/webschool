# Generated by Django 3.0.7 on 2020-07-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create_Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.CharField(max_length=20)),
                ('school_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('est_year', models.CharField(max_length=255)),
                ('school_type', models.CharField(max_length=255)),
                ('lowest_level', models.CharField(max_length=255)),
                ('topest_level', models.CharField(max_length=255)),
                ('cover_pic', models.ImageField(upload_to='images')),
                ('prove_pic', models.ImageField(upload_to='images')),
                ('admin_code', models.CharField(max_length=8)),
                ('teacher_code', models.CharField(max_length=8)),
                ('student_code', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Joined_Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_user_id', models.CharField(max_length=10)),
                ('school_id', models.CharField(max_length=20)),
                ('school_name', models.CharField(max_length=100)),
                ('joined_user_type', models.CharField(max_length=100)),
                ('joined_school_pic', models.ImageField(upload_to='images')),
            ],
        ),
    ]
