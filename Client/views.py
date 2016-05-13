from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.conf.urls import url
from ldap3 import *
import hashlib
import json
from hmsapp.models import Patient,Physician,Native,Sessionlist
import requests
import uuid

# Create your views here.


def oauthLogin(request):
    #Base URL
    urlxx = request.build_absolute_uri();
    urlxx = urlxx[:-8];


    # Search
    if request.POST.get('PIDSubmit','') != '':
        r = requests.get(urlxx+"/patients/id/"+request.POST.get('PID', '')+"/", headers={'Authorization':'bearer '+request.POST.get('token', '')});
        if '<!DOCTYPE html>' not in r.text:
            return render(request, 'client/searchMain.html', {'token': request.POST.get('token', ''), 'Plist': r.text})
        else:
            return render(request, 'client/searchMain.html', {'token': request.POST.get('token', ''), 'Plist': "Authentication Error"})
    error=0;
    if request.POST.get('type','') == 'ldap':
        if request.POST.get('submission', '') != '' :
            server = Server(request.POST.get('server',''));
            conn  = Connection(server, 'cn='+request.POST.get('username','')+', dc=acme, dc=com', request.POST.get('password',''))
            conn2 = Connection(server, 'cn='+request.POST.get('username','')+'+userPassword='+request.POST.get('password','')+',ou=Users,dc=acme,dc=com',request.POST.get('password',''))

            session_id = uuid.uuid1()
            s = Sessionlist(session_id = session_id);
            s.save();
            if(conn.bind()==True):
                return render(request, 'client/loginsuccess.html', {'session_id':session_id})
            elif(conn2.bind()==True):
                return render(request, 'client/loginsuccess.html', {'session_id':session_id})

            error=1;

        return render(request, 'client/login.html',{'error':error})

    if request.POST.get('type','') == 'oauth':

        username = request.POST.get('username', '');
        password = request.POST.get('password', '');
        client_id = request.POST.get('clientID', '');
        client_secret = request.POST.get('clientSecret', '');
        result = {'access_token': ""}


        # If Access Token is able to use
        if request.POST.get('submission', '') != '' :
            r = requests.get(urlxx+"/patients/", headers={'Authorization':'bearer '+request.POST.get('token', '')});
            if 'Authentication' not in r.text:
                return render(request, 'client/searchMain.html', {'token': request.POST.get('token', ''), 'Plist':"(none)"})

        # login attempt
        if username != '' :
	    
            print(urlxx+'/o/token/')
            response = requests.post(
                urlxx+'/o/token/',
                data={
                    'grant_type': 'password',
                    'username': username,
                    'password': password,
                    'client_id': client_id,
                    'client_secret': client_secret
                }
            )
            if "access_token" not in response.text:
                result = {'access_token': "ERROR"}
                error=1;
            else:
                result = json.loads(response.text)

        return render(request, 'client/login.html', {'token': result['access_token'], 'error':error})

    #native Login
    if request.POST.get('type','') == 'native':
        username = request.POST.get('username', '');
        password = request.POST.get('password', '');
        m = hashlib.md5()
        m.update(password.encode('utf8'))
        password = m.hexdigest()
        q = Native.objects.filter(username=username,password=password);


        if len(q) > 0:

            session_id = uuid.uuid1();
            v = Native.objects.get(username=username);
            v.session_id=session_id;
            v.save();

            s = Sessionlist(session_id = session_id);
            s.save();


            return render(request, 'client/loginsuccess.html', {'session_id':session_id})
        error = 1;

    return render(request, 'client/login.html',{'error':error});
