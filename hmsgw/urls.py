
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin


admin.autodiscover()

from securityservice.models import ssuser,ctloc

from rest_framework import permissions, routers, serializers, viewsets, generics
from rest_framework import filters

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


from Client import views as client_view

from securityservice import views as dataprovider_view




# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'securityservice', dataprovider_view.SecurityServiceViewSet,'securityservice')
#router.register(r'ctloc', dataprovider_view.CtlocViewSet,'ctloc')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
	url(r'^', include(router.urls)),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^docs/', include('rest_framework_swagger.urls')),

	# Users login
	url(r'^Client/', client_view.oauthLogin, name='oauthLogin'),

	#Web Quey
	url(r'^', include('webquery.urls')),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

