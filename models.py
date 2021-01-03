from django.db import models

class User(models.Model):
    name_of_user = models.CharField(max_length=200)
    possition_of_user = models.CharField(max_length=200)
    age_of_user=models.IntegerField(max_length=500)
    def __str__(self):
        return self.name_of_user
# Create your models here.
