from django.db import models

# Create your models here.
class Report(models.Model):
    Patient_name=models.CharField(max_length=200)
    Aadhar_Number=models.CharField(max_length=12)
    Email = models.CharField(max_length=200)
    Age = models.IntegerField(default=0)
    Sex = models.CharField(max_length=5)
    Phone_number = models.CharField(max_length=10)
    Bill_no = models.IntegerField(unique=True)
    CR_no = models.IntegerField()
    Report = models.ImageField(upload_to='report/%Y/%m/%d/',max_length=255,null=True,blank=True)
    Test_name = models.CharField(max_length=200)
    Medlab_name=models.CharField(max_length=200)
    Date_of_report = models.DateTimeField()
    def __str__(self):
        return self.Patient_name