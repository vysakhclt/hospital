from django.contrib import admin
from .models import Doctors, Blog,Booking

# Register your models here.

admin.site.register(Doctors)
admin.site.register(Blog)
admin.site.register(Booking)
