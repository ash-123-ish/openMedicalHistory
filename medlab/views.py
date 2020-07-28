# Create your views here.
from django.shortcuts import render
from random import randint
from datetime import datetime
# Create your views here.
from medlab.models import Report


def patient(request):
    return render(request,'medlab_first.html')

def register(request):
    Patient_name = request.POST['patient_name']
    Aadhar_Number = request.POST['aadhar_number']
    Age = request.POST['age']
    Sex = request.POST['gender']
    Phone_number = request.POST['phone_number']
    Bill_no = randint(100000,999999)
    CR_no = request.POST['cr_no']
    Medlab_name = request.POST['medlab_name']
    Email = request.POST['email']
    Date_of_report = datetime.today()
    r=Report(Patient_name = Patient_name,Aadhar_Number = Aadhar_Number,Email = Email,Age = Age,Sex = Sex,Phone_number = Phone_number,Bill_no = Bill_no,CR_no = CR_no,Medlab_name = Medlab_name,Date_of_report = Date_of_report)
    r.save()
    return render(request,'DatabaseStatus2.html',{'Bill_no':Bill_no , 'CR_no':CR_no})

def patientreport(request):
    return render(request,'medlabLogin.html')

def publishReport(request,bill_no):
    Test_name = request.POST['test_name']
    report_image = request.FILES['report']
    r = Report.objects.get(Bill_no = bill_no)
    r.Test_name = Test_name;
    r.Report = report_image
    r.save()
    return  render(request,'ReportStatus.html',{'report':r})

def login(request):
    billno = request.POST['billno']
    r=Report.objects.get(Bill_no = billno)
    return render(request,'publish_medlab.html',{'report':r})

def reportview(request):
    return render(request,'')