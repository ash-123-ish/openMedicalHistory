from django.urls import path

from doctor import views

urlpatterns = [
    path('',views.login,name="HospitalLoginPage"),
    path('register_Patient',views.register,name="HospitalRegisterPatientPage"),
    path('addDatabase',views.addDatabase,name="DatabaseStatusPage"),
    path('homepage',views.homepage,name="HomePage"),
    path('report',views.result,name="ResultPage"),
    path('logindoctor',views.logindoctor,name="LoginDoctorPage"),
    path('patientview',views.patientview,name="PatientViewPage"),
    path('<int:cr_no>/publishimage',views.publishimage,name="PublishPage"),
]