from django.db import models

# Create your models here.
class User(models.Model):
     First_Name =models.CharField(max_length=40)
     Second_Name =models.CharField(max_length=40)
     Email=models.EmailField(max_length=20)
     def __str__(self):
         return self.First_Name




class Newdrug(models.Model):
    Name=models.CharField(max_length=40)
    cover =models.ImageField(upload_to="media")
    Price =models.IntegerField()
    def __str__(self):
        return self.Name