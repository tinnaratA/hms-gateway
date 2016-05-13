# Hms-Gateway
## Concept
  HMS Gateway will be the gateway which will give an authentication data verification for each applications that connected to the gateway.
  The gateway is trended to be a single gateway to provide HIS's data services to regacy appliations. As a resul there are difference number of HIS((TrakCare, B-Connect, I-Med) being deployed thoughout the country. 

## How to Install:
0. Python Install These Dependencies:
    - Django==1.9.6
    - django-braces==1.8.1
    - django-oauth-toolkit==0.10.0
    - django-rest-swagger==0.3.6
    - djangorestframework==3.3.3
    - ldap3==1.2.2
    - oauthlib==1.0.3
    - psycopg2==2.6.1
    - pyasn1==0.1.9
    - PyYAML==3.11
    - requests==2.10.0

1.	Create Migration
	- Python manage.py createmigrations
    - Python manage.py migrate

2.	Create Super User
    - Python manage.py create superuser
                
3.	Connect to https//localhost:8000/admin
    - Create User
    - Create App Credentials
        * Home › Django OAuth Toolkit › Applications
        * Create type = public, grant Type = resource owner password based
        * Input other data 

4.	OAuth Authentication

## How to connect to get data:

    curl -d "client_id=app01_id&client_secret=app01_secret&grant_type=password&username=app01&password=p@ssw0rd&scope=read" http://dev-hms.bdms.co.th/o/token/”


## Connect to Main Page (http://localhost:8000/)
- SS User Data
    - http://localhost:8000/ssuser/
    - http://localhost:8000/ssuser/?ssusr_initials=001000002&ssusr_password=001000002
                
- CT Loc Data
    - http://localhost:8000/ctloc/
    - http://localhost:8000/ctloc/?ctloc_code=01W9D
- Get Data By sending get request with tokens:
    - curl -X GET -H "Authorization: Bearer xHgGDbrUjIXY3S5znyQu3r8NkbjmjG" "http://dev-hms.bdms.co.th/ssuser/?ssusr_initials=xxx&ssusr_password=yyy"

 
