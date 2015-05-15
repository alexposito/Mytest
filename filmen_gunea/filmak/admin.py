from filmak.models import filma
from filmak.models import bozkatzailea

from django.contrib import admin

class filmaAdmin(admin.ModelAdmin):
    fields = ['izenburua', 'zuzendaria', 'urtea', 'generoa', 'sinopsia', 'bozkak']
admin.site.register(filma, filmaAdmin)

class bozkatzaileaAdmin(admin.ModelAdmin):
    fields = ['erabiltzailea_id', 'gogoko_filmak']

admin.site.register(bozkatzailea, bozkatzaileaAdmin)
