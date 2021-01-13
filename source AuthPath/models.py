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
