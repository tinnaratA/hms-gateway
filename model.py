# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataproviderCtloc(models.Model):
    ctloc_rowid = models.IntegerField(primary_key=True)
    ctloc_code = models.CharField(max_length=220)
    ctloc_desc = models.CharField(max_length=220, blank=True, null=True)
    ctloc_glccc_dr = models.IntegerField(blank=True, null=True)
    ctloc_password = models.CharField(max_length=220, blank=True, null=True)
    ctloc_wardflag = models.CharField(max_length=220, blank=True, null=True)
    ctloc_address = models.CharField(max_length=4096, blank=True, null=True)
    ctloc_activeflag = models.CharField(max_length=220, blank=True, null=True)
    ctloc_cashier_dr = models.IntegerField(blank=True, null=True)
    ctloc_otc_dr = models.IntegerField(blank=True, null=True)
    ctloc_starttime = models.TimeField(blank=True, null=True)
    ctloc_endtime = models.TimeField(blank=True, null=True)
    ctloc_ownqueflag = models.CharField(max_length=220, blank=True, null=True)
    ctloc_recqueflag = models.CharField(max_length=220, blank=True, null=True)
    ctloc_type = models.CharField(max_length=220, blank=True, null=True)
    ctloc_disploc_dr = models.IntegerField(blank=True, null=True)
    ctloc_floor = models.CharField(max_length=220, blank=True, null=True)
    ctloc_nfmi_dr = models.CharField(max_length=254, blank=True, null=True)
    ctloc_laundry = models.CharField(max_length=220, blank=True, null=True)
    ctloc_dep_dr = models.IntegerField(blank=True, null=True)
    ctloc_differentsexpatients = models.CharField(max_length=220, blank=True, null=True)
    ctloc_index = models.CharField(max_length=220, blank=True, null=True)
    ctloc_hospital_dr = models.IntegerField(blank=True, null=True)
    ctloc_executeconfirmation = models.CharField(max_length=220, blank=True, null=True)
    ctloc_dateactivefrom = models.DateField()
    ctloc_dateactiveto = models.DateField(blank=True, null=True)
    ctloc_rehabilitativeflag = models.CharField(max_length=220, blank=True, null=True)
    ctloc_medicalrecordactive = models.CharField(max_length=220, blank=True, null=True)
    ctloc_defaultmrtype_dr = models.IntegerField(blank=True, null=True)
    ctloc_resultdelivery = models.CharField(max_length=220, blank=True, null=True)
    ctloc_respunit_dr = models.IntegerField(blank=True, null=True)
    ctloc_patientagesexmix_dr = models.IntegerField(blank=True, null=True)
    ctloc_intendclincareintensity_dr = models.IntegerField(blank=True, null=True)
    ctloc_broadpatientgroup_dr = models.IntegerField(blank=True, null=True)
    ctloc_weeklyavailindicator = models.CharField(max_length=220, blank=True, null=True)
    ctloc_openovernightindicator = models.CharField(max_length=220, blank=True, null=True)
    ctloc_signiffacility_dr = models.IntegerField(blank=True, null=True)
    ctloc_notused = models.CharField(max_length=220, blank=True, null=True)
    ctloc_extgroup_dr = models.IntegerField(blank=True, null=True)
    ctloc_externalinfosystem = models.CharField(max_length=220, blank=True, null=True)
    ctloc_telephone = models.CharField(max_length=220, blank=True, null=True)
    ctloc_telephoneext = models.CharField(max_length=220, blank=True, null=True)
    ctloc_hl7orderslink = models.CharField(max_length=220, blank=True, null=True)
    ctloc_contactname = models.CharField(max_length=220, blank=True, null=True)
    ctloc_floorplanquery = models.CharField(max_length=220, blank=True, null=True)
    ctloc_visithrfrom = models.TimeField(blank=True, null=True)
    ctloc_visithrto = models.TimeField(blank=True, null=True)
    ctloc_restperiodfrom = models.TimeField(blank=True, null=True)
    ctloc_restperiodto = models.TimeField(blank=True, null=True)
    ctloc_agefrom = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ctloc_ageto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ctloc_nationcode = models.CharField(max_length=220, blank=True, null=True)
    ctloc_orderstorecloc = models.CharField(max_length=220, blank=True, null=True)
    ctloc_sendhl7messageon = models.CharField(max_length=220, blank=True, null=True)
    ctloc_departmentheaduserdr = models.IntegerField(blank=True, null=True)
    ctloc_pagerno = models.CharField(max_length=220, blank=True, null=True)
    ctloc_email = models.CharField(max_length=220, blank=True, null=True)
    ctloc_fax = models.CharField(max_length=220, blank=True, null=True)
    ctloc_daysautogenerate = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_mrrequestmovevalid = models.CharField(max_length=220, blank=True, null=True)
    ctloc_snapflag = models.CharField(max_length=220, blank=True, null=True)
    ctloc_multdaterangesvisithrs = models.CharField(max_length=230, blank=True, null=True)
    ctloc_mentalhealthunit = models.CharField(max_length=220, blank=True, null=True)
    ctloc_preferedoutlierward = models.IntegerField(blank=True, null=True)
    ctloc_wardsinglesex = models.IntegerField(blank=True, null=True)
    ctloc_printlabelsurgmrrequest = models.CharField(max_length=220, blank=True, null=True)
    ctloc_enabledischargeallhyperlink = models.CharField(max_length=220, blank=True, null=True)
    ctloc_inpatientunit = models.CharField(max_length=220, blank=True, null=True)
    ctloc_outpatientunit = models.CharField(max_length=220, blank=True, null=True)
    ctloc_timesincelastappt = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_period = models.CharField(max_length=220, blank=True, null=True)
    ctloc_dischsumnotrequired = models.CharField(max_length=220, blank=True, null=True)
    ctloc_natcodedatefrom = models.DateField(blank=True, null=True)
    ctloc_natcodedateto = models.DateField(blank=True, null=True)
    ctloc_signfacildatefrom = models.DateField(blank=True, null=True)
    ctloc_signiffacildateto = models.DateField(blank=True, null=True)
    ctloc_dischargelounge = models.CharField(max_length=220, blank=True, null=True)
    ctloc_externalviewerlink = models.CharField(max_length=220, blank=True, null=True)
    ctloc_daystokeeprecord = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_nataheadings = models.CharField(max_length=4096, blank=True, null=True)
    ctloc_weekssuspensionreview = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_daysforopdoffer = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_daysforopletterresponse = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_offersbeforeip_opwaitreset = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_daysofferoutcomechange = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctloc_radordaccessnoprefix = models.CharField(max_length=220, blank=True, null=True)
    ctloc_donotdisplayroomdescforbed = models.CharField(max_length=220, blank=True, null=True)
    ctloc_ebookerid = models.CharField(max_length=220, blank=True, null=True)
    ctloc_ebookingid = models.CharField(max_length=220, blank=True, null=True)
    ctloc_ebookerenabled = models.CharField(max_length=220, blank=True, null=True)
    ctloc_ebookingenabled = models.CharField(max_length=220, blank=True, null=True)
    ctloc_ebookeriurpenabled = models.CharField(max_length=220, blank=True, null=True)
    ctloc_ebookersuspdate = models.DateField(blank=True, null=True)
    ctloc_ebookersuspreas = models.CharField(max_length=4096, blank=True, null=True)
    ctloc_dischsumoprequired = models.CharField(max_length=220, blank=True, null=True)
    ctloc_dischsumiprequired = models.CharField(max_length=220, blank=True, null=True)
    ctloc_dischsumedrequired = models.CharField(max_length=220, blank=True, null=True)
    ctloc_ipdischsummarytype = models.CharField(max_length=220, blank=True, null=True)
    ctloc_opdischsummarytype = models.CharField(max_length=220, blank=True, null=True)
    ctloc_eddischsummarytype = models.CharField(max_length=220, blank=True, null=True)
    ctloc_chargeaccompatientonleave = models.CharField(max_length=220, blank=True, null=True)
    ctloc_communityunit = models.CharField(max_length=220, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataprovider_ctloc'


class DataproviderSsuser(models.Model):
    ssusr_rowid = models.IntegerField(primary_key=True)
    ssusr_initials = models.CharField(max_length=220)
    ssusr_name = models.CharField(max_length=220)
    ssusr_password = models.CharField(max_length=220)
    ssusr_defaultdept_dr = models.IntegerField(blank=True, null=True)
    ssusr_isthisdoctor = models.CharField(max_length=220, blank=True, null=True)
    ssusr_usedeptasdefault = models.CharField(max_length=220, blank=True, null=True)
    ssusr_ctpcp_dr = models.CharField(max_length=220, blank=True, null=True)
    ssusr_group = models.IntegerField()
    ssusr_changelocation = models.CharField(max_length=220, blank=True, null=True)
    ssusr_emailname = models.CharField(max_length=220, blank=True, null=True)
    ssusr_deptforemrlists = models.IntegerField(blank=True, null=True)
    ssusr_ctlan_dr = models.IntegerField(blank=True, null=True)
    ssusr_careprov_dr = models.CharField(max_length=220, blank=True, null=True)
    ssusr_pin = models.CharField(max_length=220, blank=True, null=True)
    ssusr_privilegestock = models.CharField(max_length=220, blank=True, null=True)
    ssusr_retainordercategory = models.CharField(max_length=220, blank=True, null=True)
    ssusr_lastpaadm_dr = models.IntegerField(blank=True, null=True)
    ssusr_active = models.CharField(max_length=220, blank=True, null=True)
    ssusr_drgtariffvisible = models.CharField(max_length=220, blank=True, null=True)
    ssusr_billsequence_dr = models.IntegerField(blank=True, null=True)
    ssusr_searchalladm = models.CharField(max_length=220, blank=True, null=True)
    ssusr_inpatient = models.CharField(max_length=220, blank=True, null=True)
    ssusr_outpatient = models.CharField(max_length=220, blank=True, null=True)
    ssusr_emergency = models.CharField(max_length=220, blank=True, null=True)
    ssusr_ownpatientsonly = models.CharField(max_length=220, blank=True, null=True)
    ssusr_loclist_dr = models.IntegerField(blank=True, null=True)
    ssusr_autoauthorise = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defaultarcim_dr = models.CharField(max_length=254, blank=True, null=True)
    ssusr_defrbdepartment_dr = models.IntegerField(blank=True, null=True)
    ssusr_defrbresource_dr = models.IntegerField(blank=True, null=True)
    ssusr_defrbservice_dr = models.IntegerField(blank=True, null=True)
    ssusr_defepisode = models.CharField(max_length=220, blank=True, null=True)
    ssusr_linktobedmanagement = models.CharField(max_length=220, blank=True, null=True)
    ssusr_usedefaultepisdep = models.CharField(max_length=220, blank=True, null=True)
    ssusr_warnorbookingmoveres = models.CharField(max_length=220, blank=True, null=True)
    ssusr_nallorbookpast = models.CharField(max_length=220, blank=True, null=True)
    ssusr_nallorbooknosess = models.CharField(max_length=220, blank=True, null=True)
    ssusr_nallorbookna = models.CharField(max_length=220, blank=True, null=True)
    ssusr_alwaysusesoundex = models.CharField(max_length=220, blank=True, null=True)
    ssusr_rbnumberofrows = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ssusr_multiselectrows = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ssusr_passworddate = models.DateField(blank=True, null=True)
    ssusr_datelastlogin = models.DateField(blank=True, null=True)
    ssusr_timelastlogin = models.TimeField(blank=True, null=True)
    ssusr_datefromtoday = models.CharField(max_length=220, blank=True, null=True)
    ssusr_datetotoday = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defrefhosp_dr = models.IntegerField(blank=True, null=True)
    ssusr_resentrybuttons = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defaultresentrybuttons = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defdateinoe = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defdateindisch = models.CharField(max_length=220, blank=True, null=True)
    ssusr_disableemrpreadm = models.CharField(max_length=220, blank=True, null=True)
    ssusr_searchprevadm = models.CharField(max_length=220, blank=True, null=True)
    ssusr_noorders = models.CharField(max_length=220, blank=True, null=True)
    ssusr_noemr = models.CharField(max_length=220, blank=True, null=True)
    ssusr_nodiagnosis = models.CharField(max_length=220, blank=True, null=True)
    ssusr_websecurityaccess = models.CharField(max_length=220, blank=True, null=True)
    ssusr_epissubtype_dr = models.IntegerField(blank=True, null=True)
    ssusr_notreadresults = models.CharField(max_length=220, blank=True, null=True)
    ssusr_restrictmodifdischarge = models.CharField(max_length=220, blank=True, null=True)
    ssusr_booked = models.CharField(max_length=220, blank=True, null=True)
    ssusr_admitted = models.CharField(max_length=220, blank=True, null=True)
    ssusr_discharged = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defaultcareprov = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defaultlocation = models.CharField(max_length=220, blank=True, null=True)
    ssusr_passwordchanged = models.CharField(max_length=220, blank=True, null=True)
    ssusr_title = models.CharField(max_length=220, blank=True, null=True)
    ssusr_surname = models.CharField(max_length=220, blank=True, null=True)
    ssusr_givenname = models.CharField(max_length=220, blank=True, null=True)
    ssusr_othername = models.CharField(max_length=220, blank=True, null=True)
    ssusr_departmenthead = models.CharField(max_length=220, blank=True, null=True)
    ssusr_payrollnumber = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ssusr_stafftype_dr = models.IntegerField(blank=True, null=True)
    ssusr_comments = models.CharField(max_length=4096, blank=True, null=True)
    ssusr_lastupdateuser_dr = models.IntegerField(blank=True, null=True)
    ssusr_lastupdatedate = models.DateField(blank=True, null=True)
    ssusr_lastupdatetime = models.TimeField(blank=True, null=True)
    ssusr_doctorflag = models.CharField(max_length=220, blank=True, null=True)
    ssusr_nurseflag = models.CharField(max_length=220, blank=True, null=True)
    ssusr_securitymsgread = models.CharField(max_length=220, blank=True, null=True)
    ssusr_securitymessage = models.CharField(max_length=4096, blank=True, null=True)
    ssusr_loginid = models.CharField(max_length=220, blank=True, null=True)
    ssusr_loginround = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defallresources = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defapptslots = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defusestarttimeeachday = models.CharField(max_length=220, blank=True, null=True)
    ssusr_defappointmeth_dr = models.IntegerField(blank=True, null=True)
    ssusr_title_dr = models.IntegerField(blank=True, null=True)
    ssusr_registrationnumber = models.CharField(max_length=220, blank=True, null=True)
    ssusr_printsecuritylevel = models.CharField(max_length=220, blank=True, null=True)
    ssusr_lastupdateuserhosp_dr = models.IntegerField(blank=True, null=True)
    ssusr_changelocwithinloghosp = models.CharField(max_length=220, blank=True, null=True)
    ssusr_notallowtooverbook = models.CharField(max_length=220, blank=True, null=True)
    ssusr_markinactivedate = models.DateField(blank=True, null=True)
    ssusr_markinactivetime = models.TimeField(blank=True, null=True)
    ssusr_markinactiveuser_dr = models.IntegerField(blank=True, null=True)
    ssusr_datefrom = models.DateField(blank=True, null=True)
    ssusr_dateto = models.DateField(blank=True, null=True)
    ssusr_hospital_dr = models.IntegerField(blank=True, null=True)
    ssusr_mobile = models.CharField(max_length=220, blank=True, null=True)
    ssusr_pager = models.CharField(max_length=220, blank=True, null=True)
    ssusr_email = models.CharField(max_length=220, blank=True, null=True)
    ssusr_locationnotmandatoryonresentry = models.CharField(max_length=220, blank=True, null=True)
    ssusr_timesincelastappt = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ssusr_timesinceperiod = models.CharField(max_length=220, blank=True, null=True)
    ssusr_name1 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_name2 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_name3 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_iepath = models.CharField(max_length=220, blank=True, null=True)
    ssusr_externaluseridentifier = models.CharField(max_length=220, blank=True, null=True)
    ssusr_cashiershift = models.CharField(max_length=220, blank=True, null=True)
    ssusr_biokey = models.CharField(max_length=220, blank=True, null=True)
    ssusr_biomode = models.CharField(max_length=220, blank=True, null=True)
    ssusr_disclaimersigned = models.DateField(blank=True, null=True)
    ssusr_createdby_dr = models.IntegerField(blank=True, null=True)
    ssusr_createddate = models.DateField(blank=True, null=True)
    ssusr_createdtime = models.TimeField(blank=True, null=True)
    ssusr_yesno1 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_yesno2 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_yesno3 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_yesno4 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_yesno5 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_freetext1 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_freetext2 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_freetext3 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_allowweblayoutmanager = models.CharField(max_length=220, blank=True, null=True)
    ssusr_allowwebcolumnmanager = models.CharField(max_length=220, blank=True, null=True)
    ssusr_externalid2 = models.CharField(max_length=220, blank=True, null=True)
    ssusr_treatmentpathwayowner = models.CharField(max_length=220, blank=True, null=True)
    ssusr_treatmentstageowner = models.CharField(max_length=220, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataprovider_ssuser'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HmsappNative(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    password = models.CharField(max_length=32)
    gender = models.CharField(max_length=40)
    session_id = models.CharField(max_length=80)
    session_expired = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hmsapp_native'


class HmsappPatient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    blood_type = models.CharField(max_length=2)
    allergies = models.TextField()

    class Meta:
        managed = False
        db_table = 'hmsapp_patient'


class HmsappPhysician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    specialise = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    address = models.TextField()

    class Meta:
        managed = False
        db_table = 'hmsapp_physician'


class HmsappSessionlist(models.Model):
    session_id = models.CharField(max_length=80)
    session_expired = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hmsapp_sessionlist'


class Oauth2ProviderAccesstoken(models.Model):
    token = models.CharField(max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderApplication(models.Model):
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    skip_authorization = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_application'


class Oauth2ProviderGrant(models.Model):
    code = models.CharField(max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=255)
    scope = models.TextField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderRefreshtoken(models.Model):
    token = models.CharField(max_length=255)
    access_token = models.ForeignKey(Oauth2ProviderAccesstoken, models.DO_NOTHING, unique=True)
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'
