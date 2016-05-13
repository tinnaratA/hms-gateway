# Register your models here.
from django.contrib import admin
from .models import Patient,Physician,Native,Sessionlist
# Register your models here.
admin.site.register(Patient)
admin.site.register(Physician)
admin.site.register(Native)
admin.site.register(Sessionlist)
