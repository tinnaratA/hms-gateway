from rest_framework import serializers
from dataprovider.models import ctloc,ssuser


class CtlocSerializer(serializers.ModelSerializer):
	class Meta:
		model = ctloc
		fields = ('ctloc_rowid','ctloc_code','ctloc_desc','ctloc_type')
		
class SsuserSerializer(serializers.ModelSerializer):
	deptdata = CtlocSerializer(source = "ssusr_defaultdept_dr")
	class Meta:
		model = ssuser
		fields = ('ssusr_rowid', 'ssusr_initials','ssusr_name','ssusr_password','ssusr_defaultdept_dr','ssusr_dateto','ssusr_group','deptdata')
		

