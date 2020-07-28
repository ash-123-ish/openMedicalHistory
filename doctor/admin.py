from django.contrib import admin

# Register your models here.
from doctor.models import Prescription

admin.site.register(Prescription)