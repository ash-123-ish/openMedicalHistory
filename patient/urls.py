from django.urls import path

from patient import views

urlpatterns=[
    path('',views.login,name='login'),
    path('patientlogin',views.patientlogin,name="PatientCounter"),
    path('report',views.report,name='report'),
    path('record',views.record,name='record'),
    path('PatientRegistration',views.register,name="PatientRegistration"),
    path('profile',views.profile,name="ProfilePatient"),
]