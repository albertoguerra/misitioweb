from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'misitioweb.views.home', name='home'),
    # url(r'^misitioweb/', include('misitioweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = patterns('blog.views',
    (r"^entrada/(?P<pk>\d+)/$","entrada"),
    (r"^poncomentario/(\d+)/$","poncomentario"),
    (r'^admin/', include(admin.site.urls)),

    (r"","main"),

)
