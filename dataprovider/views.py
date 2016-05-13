from django.shortcuts import render

from rest_framework import permissions, routers, serializers, viewsets, generics
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from dataprovider.models import ctloc,ssuser
from dataprovider.serializers import CtlocSerializer,SsuserSerializer

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from .TrakcareEncrypt import *



class CtlocViewSet(viewsets.ModelViewSet):
	serializer_class = CtlocSerializer
	def get_queryset(self):
		queryset = ctloc.objects.all()
		ctloc_code = self.request.query_params.get('ctloc_code', None)
		if ctloc_code is not None:
			queryset = ctloc.objects.filter(ctloc_code=ctloc_code)
		
		return queryset
	
class SsuserViewSet(viewsets.ModelViewSet):
	serializer_class = SsuserSerializer
	def get_queryset(self):
		queryset = ssuser.objects.all()
		ssusr_initials = self.request.query_params.get('ssusr_initials', None)
		ssusr_password = self.request.query_params.get('ssusr_password', None)
		
		if ssusr_initials is not None and ssusr_password is not None :
			ssusr_password = Trakcare_encrypt(ssusr_password)
			queryset = ssuser.objects.filter(ssusr_initials=ssusr_initials,ssusr_password=ssusr_password)
		
		return queryset
	