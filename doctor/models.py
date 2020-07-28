from django.db import models

# Create your models here.
class Prescription(models.Model):
    Patient_name= models.CharField(max_length=200)
    Aadhar_number=models.CharField(max_length=12)
    Email = models.CharField(max_length=200)
    Age = models.IntegerField(default=0)
    Sex = models.CharField(max_length=5)
    Phone_number = models.CharField(max_length=10)
    Address = models.CharField(max_length=200)
    CR_no = models.IntegerField()
    Prescription = models.ImageField(upload_to='prescription/%Y/%m/%d/',max_length=255,null=True,blank=True)
    Prescription_text = models.CharField(max_length = 2000)
    Online_status = models.IntegerField(default = 0)
    Diagnosis = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)
    Doctor_name = models.CharField(max_length=200)
    Doctor_dept = models.CharField(max_length=200)
    Date_of_meeting = models.DateTimeField()
    def __str__(self):
        return self.Patient_name