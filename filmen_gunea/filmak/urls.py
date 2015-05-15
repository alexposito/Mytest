from django.conf.urls import patterns, url

urlpatterns = patterns('filmak.views',
    url(r'hasiera$', 'hasiera', name='hasiera'),
    url(r'ikusi$', 'ikusi', name='ikusi'),
    url(r'bozkatu$', 'bozkatu', name='bozkatu'),
    url(r'bozkak/(?P<filmId>\d+)$', 'bozkak', name='bozkak'),
)
