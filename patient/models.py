from django.db import models

# Create your models here.
class Patient(models.Model):
    Name = models.CharField(max_length=200)
    Aadhar_Number = models.CharField(max_length=200);
    Email = models.CharField(max_length=200);
    Profile_pic = models.ImageField(upload_to='profiles/',max_length=255,null=True,blank=True)
    Phone_Number = models.CharField(max_length=200);
    Age = models.IntegerField(default=0);
    Sex = models.CharField(max_length=5);
    def __str__(self):
            return self.Name