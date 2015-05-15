from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class filma(models.Model):
    # Atributuak
    izenburua = models.CharField(max_length=100)
    zuzendaria = models.CharField(max_length=60)
    urtea = models.IntegerField()
    generoa = models.CharField(max_length=20)
    sinopsia = models.CharField(max_length=500)
    bozkak = models.IntegerField()
    def __unicode__(self):
        return self.izenburua

class bozkatzailea(models.Model):
    #Loturak
    erabiltzailea_id = models.OneToOneField(User)
    gogoko_filmak = models.ManyToManyField(filma)
