from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mcash_store.views.home', name='home'),
    url(r'^pay/$', 'mcash_store.views.do_payment_request', name='do_payment_request'),
    url(r'^payment_response/$', 'mcash_store.views.payment_response', name='payment_response'),
    url(r'^payment_capture_response/$', 'mcash_store.views.payment_capture_response', name='payment_capture_response'),

    # Examples:
    # url(r'^$', 'mcash_store.views.home', name='home'),
    # url(r'^mcash_store/', include('mcash_store.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
