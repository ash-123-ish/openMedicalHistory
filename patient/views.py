from django.shortcuts import render
from doctor.models import Prescription
from medlab.models import Report
from patient.models import Patient
# Create your views here.
def login(request):
    return render(request,'login.html')

def report(request):
    billno=request.POST['BillNo']
    crno = request.POST['CRNo']
    p = Prescription.objects.get(CR_no = crno)
    r = Report.objects.get(Bill_no = billno)
    return  render(request,'report.html',{'Object':p,'report':r})

def patientlogin(request):
    return render(request,'Patient_Login.html')

def record(request):
    Name=request.POST['Name']
    Aadhar_Number=request.POST['Aadhar_Number']
    Email=request.POST['email']
    Profile_pic=request.FILES['profile']
    Phone_Number=request.POST['Phone_Number']
    Age=request.POST['Age']
    Sex=request.POST['Sex']
    pat=Patient(Name=Name,Aadhar_Number=Aadhar_Number,Email=Email,Profile_pic=Profile_pic,Phone_Number=Phone_Number,Age=Age,Sex=Sex)
    pat.save()
    return render(request,'Patient_Login.html')

def register(request):
    return render(request,'PatientRegistration.html')

def profile(request):
    return render(request,'patientdashboard.html')