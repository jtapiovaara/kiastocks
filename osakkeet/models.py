from django.db import models


class Osakkeet(models.Model):
    nimi = models.CharField(max_length=64)
    porssinimi = models.CharField(max_length=24)
    maara = models.IntegerField(default=1)
    alkuarvo = models.IntegerField(default=1)
    arvo = models.IntegerField(default=1)
    osingot = models.IntegerField(default=1)
    salkunarvo = models.IntegerField(default=1)
    salkunverot = models.IntegerField(default=1)
    verovuosi = models.IntegerField(default=2010)

    def __str__(self):
        return self.nimi

    class Meta:
        ordering = ('nimi',)
