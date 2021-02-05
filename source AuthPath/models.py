from django.db import models

class User(models.Model):
    name_of_user = models.CharField(max_length=200)
    possition_of_user = models.CharField(max_length=200)
    email_of_user = models.EmailField()
    date_of_birth_of_user = models.DateField(auto_now=False)
    main_photo = models.ImageField(upload_to='main/photos_of_users', height_field=None, width_field=None, max_length=100)
    describtion_of_user = models.TextField(max_length=670)
    login_of_user = models.CharField(max_length=200 ,default='')
    password_of_user = models.CharField(max_length=200,default='')
  
    age_of_user=models.IntegerField()
    def __str__(self):
        return self.name_of_user

# Create your models here.

#table of accounting 

class Accounting(models.Model):
    end_of_session=models.CharField(max_length=200)
    employee=models.CharField(max_length=100)
    def __str__(self):
        return self.end_of_session

#table of Posts , post is task for today
class Post(models.Model):
    title_of_post = models.CharField(max_length=140)
    date_of_post = models.DateField(auto_now=False)
    text_of_post = models.TextField(max_length=350)
    remark_of_post= models.CharField(max_length=100)
    def __str__(self):
        return self.title_of_post


class Authour(models.Model):
    authour=models.CharField(max_length=100)
    def __str__(self):
        return self.authour
        
        