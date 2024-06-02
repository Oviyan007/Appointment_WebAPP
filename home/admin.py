from django.contrib import admin
from .models import Patient,Booking,Doctor
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Booking)