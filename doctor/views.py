from django.shortcuts import render, get_object_or_404
from datetime import datetime
from random import randint
from doctor.models import Prescription

# Create your views here.
def login(request):
    return render(request,'LoginDoctor.html')

def homepage(request):
    return render(request,'homepage.html')

def result(request):
    object = Prescription.objects.get(CR_no = '10101')
    return render(request,'report.html',{'Object' : object})

def register(request):
    return render(request,'hospital_first_page.html')

def addDatabase(request):
    if request.method == 'POST':
        Patient_name=request.POST['patient_name']
        Aadhar_number=request.POST['aadhar_number']
        Email=request.POST['email']
        Age = request.POST['age']
        Phone_number = request.POST['phone_number']
        Sex = request.POST['gender']
        Address = request.POST['address']
        Status = "Not Cure"
        Doctor_dept = request.POST['department']
        Doctor_name = request.POST['doctor_name']
        cr_no = randint(1000000,9999999)
        #while(Prescription.objects.get(CR_no = cr_no)):
        #    cr_no = randint(1000000, 9999999)
        Date_of_meeting = datetime.today()
        p=Prescription(Patient_name=Patient_name,Aadhar_number=Aadhar_number,Email=Email,Age=Age,Phone_number=Phone_number,Sex=Sex,Address=Address,Status=Status,Doctor_dept=Doctor_dept,Doctor_name=Doctor_name,CR_no=cr_no,Date_of_meeting=Date_of_meeting)
        p.save()
    return render(request,'DatabaseStatus.html',{'CR_no':cr_no})

def patientview(request):
    cr_no=request.POST['cr_no']
    p=Prescription.objects.get(CR_no = cr_no)
    return render(request,"hospital_publish_page.html",{'prescription':p})

def publishimage(request,cr_no):
    image = request.FILES['prescription_image']
    #p=Prescription(Patient_name = "Gajju",Age = 21, Sex = "MALE" , Phone_number = "8209406218", Address = "21,klm Marg", CR_no = "7778210", Prescription = image, Doctor_name = "Sarita Singh",Doctor_dept="Physical",Date_of_meeting = datetime.today())
    p=Prescription.objects.get(CR_no = cr_no)
    p.Prescription = image
    p.save()
    return render(request,'PrescriptionStatus.html',{'prescription':p})

def logindoctor(request):
    return  render(request,'LoginDoctor.html')