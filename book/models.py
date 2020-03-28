from django.db import models

# Create your models here.
class Hozzavalo(models.Model):
    olaj = models.ForeignKey('Olaj', on_delete=None)
    mennyiseg = models.CharField(max_length=200)

class Forgalmazo(models.Model):
    name = models.CharField(max_length=200)
    cim = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)

class Forgalmazas(models.Model):
    olaj = models.ForeignKey('Olaj', on_delete=None)
    ceg = models.ForeignKey('Forgalmazo', on_delete=None)
    kiszereles = models.CharField(max_length=200)
    ar = models.IntegerField()

class Olaj(models.Model):
    name = models.CharField(max_length=200)
    kep = models.CharField(max_length=200)
    mese = models.TextField()

class Korosztaly(models.Model):
    name = models.CharField(max_length=200)

class Hatas(models.Model):
    name = models.CharField(max_length=200)
    korosztaly = models.ForeignKey('Korosztaly', on_delete=None)
    megjegyzesek = models.TextField()

class Recept(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField()
    hozzavalok = models.ManyToManyField(Hozzavalo)
    hatasok = models.ManyToManyField(Hatas)
