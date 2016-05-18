from django.conf.urls import url
from webquery import views

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^webquery/$', views.snippet_list),
    url(r'^webquery/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^patient_info/(?P<pk>[0-9]+)/$', views.patient_info),
    url(r'^patient/$', views.patient_list),
    # url(r'^patient2/$',  views.PatientList.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
