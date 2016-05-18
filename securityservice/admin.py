
from django.contrib import admin
from .models import ssuser
from .models import ctloc

class ssuserAdmin(admin.ModelAdmin):
	list_display = ('ssusr_initials','ssusr_name','ssusr_password')
	search_fields = ['ssusr_initials', 'ssusr_name']
	

class ctlocAdmin(admin.ModelAdmin):
	list_display = ('ctloc_rowid','ctloc_code','ctloc_desc','ctloc_type')
	search_fields = ['ctloc_rowid', 'ctloc_code']
	
	
admin.site.register(ssuser,ssuserAdmin) 
admin.site.register(ctloc,ctlocAdmin) 

