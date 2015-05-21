"""
Definition of urls for zantu.
"""

from datetime import datetime
from django.conf.urls import patterns, include, url
from app.forms import BootstrapAuthenticationForm
from app.views import TourGuideListView
from app.models import Tourguide
#from django.contrib import admin, admindocs

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^seed', 'app.views.seed', name='seed'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^list',
        TourGuideListView.as_view(
            queryset=Tourguide.objects.all(),
            context_object_name='latest_poll_list',
            template_name='app/tourguidelist.html',),
        name='list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
