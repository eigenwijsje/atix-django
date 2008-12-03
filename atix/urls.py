from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^contact/', include('contact_form.urls')),
    (r'^articles/', include('articles.urls')),
)
