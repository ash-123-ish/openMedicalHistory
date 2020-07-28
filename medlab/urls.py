from django.urls import path

from medlab import views

urlpatterns =[
    path('',views.patient,name = "RegisterPage"),
    path('login',views.login,name = "loginpage"),
    path('patientreport',views.patientreport,name="patientreportpage"),
    path('patientinfo',views.patient,name = "patientinfopage"),
    path('register',views.register,name="registerpage"),
    path('<int:bill_no>/publishreport',views.publishReport,name="publishpage"),
    path('reportview',views.reportview,name="reportpage"),
]