from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html', 'extra_context':{'next':'filmak/hasiera'}}),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^filmak/', include('filmak.urls')),
    url(r'^register$', CreateView.as_view( template_name='registration/register.html', form_class= UserCreationForm , success_url='/' ), name="register"),
    # Examples:
    # url(r'^$', 'filmen_gunea.views.home', name='home'),
    # url(r'^filmen_gunea/', include('filmen_gunea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
