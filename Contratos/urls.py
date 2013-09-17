from django.conf.urls import patterns, include, url
from core.views import CargoList

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'core.views.home', name='home'),
	#url(r'^contratos/$', ContratosList, name='contratoList'),
	url(r'^novo-contrato/$', 'core.views.addContrato', name='addContrato'),
	url(r'^contratos/$', 'core.views.contratos', name='contratos'),
	url(r'^cargos/$', CargoList.as_view(), name='cargos'),	
    #url(r'^confirma/$', 'core.views.confirma', name='confirma'),      
	url(r'^novo-cargo/$', 'core.views.addCargo', name='addCargo'),	
    # Examples:
    # url(r'^$', 'Contratos.views.home', name='home'),
    # url(r'^Contratos/', include('Contratos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
