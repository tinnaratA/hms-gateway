# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from webquery.objects import Employee
from webquery.models import Snippet
from webquery.serializers import SnippetSerializer, PatientSerializer
import jaydebeapi
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def patient_info(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(snippet)
        return JSONResponse(serializer.data)

@csrf_exempt
def patient_list(request):

    conn = jaydebeapi.connect('com.intersys.jdbc.CacheDriver',
                               ['jdbc:Cache://10.88.23.56:1972/bmc-test', 'hmstest', '1234qwer'],
                               'C:\hmsgw\webquery\drivers\CacheDB.jar',)
    curs = conn.cursor()

    if request.method == 'GET':

        curs.execute("select top 100 * from SQLUser.PA_PatMas")

        arr_objects = []
        for data_row in curs.fetchall():
            arr_objects.append(Employee(data_row[0], data_row[1], data_row[2], data_row[3], data_row[4]))
            print(arr_objects)

        serializer = PatientSerializer(arr_objects, many=True)

        return JSONResponse(serializer.data)


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class PatientList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#
#
#         conn = jaydebeapi.connect('com.intersys.jdbc.CacheDriver',
#                                    ['jdbc:Cache://10.88.23.56:1972/bmc-test', 'hmstest', '1234qwer'],
#                                    'C:\\hmsgateway\\webservice\\pools\\drivers\\CacheDB.jar',)
#         curs = conn.cursor()
#         curs.execute("select top 2 * from SQLUser.PA_PatMas")
#         data_row = curs.fetchall()
#
#         conn.close()
#
#         snippets = data_row
#         serializer = PatientSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
