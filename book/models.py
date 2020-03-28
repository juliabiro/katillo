from django.db import models

# Create your models here.
class Forgalmazo(models.Model):
    name = models.CharField(max_length=200)
    cim = models.CharField(max_length=200)
    webpage = models.CharField(max_length=200, default="")
    telefon = models.CharField(max_length=200)
    class Meta:
            verbose_name_plural = 'Forgalmazók'
    def __str__(self):
        return self.name

class Forgalmazas(models.Model):
    olaj = models.ForeignKey('Olaj', on_delete=None)
    termeknev = models.CharField(max_length=200, default="")
    ceg = models.ForeignKey('Forgalmazo', on_delete=None)
    kiszereles = models.CharField(max_length=200)
    ar = models.IntegerField()
    class Meta:
            verbose_name_plural = 'Termékek'
    def __str__(self):
        return self.termeknev+": "+ self.kiszereles

class Olaj(models.Model):
    name = models.CharField(max_length=200)
    kep = models.CharField(max_length=200)
    mese = models.TextField()
    class Meta:
            verbose_name_plural = 'Olajok'
    def __str__(self):
        return self.name


class Recept(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField()
    class Meta:
            verbose_name_plural = 'Receptek'
    def __str__(self):
        return self.name

class Hatas(models.Model):
    KOROSZTALYOK=(('csecsemő','csecsemő'), ( 'kisgyerek', 'kisgyerek'), ( 'nagy gyerek','nagy gyerek' ), ( 'felnőtt', 'felnőtt' ), ( 'idős','idős' ), ( 'terhes','terhes' ))
    name = models.CharField(max_length=200)
    korosztaly =models.CharField(max_length=200,
                            choices=KOROSZTALYOK,
                            default='felnőtt') 
    megjegyzesek = models.TextField()
    recept = models.ForeignKey('Recept', on_delete=None)
    def __str__(self):
        return self.name +":"+ self.korosztaly
    class Meta:
            verbose_name_plural = 'Hatások'

class Hozzavalo(models.Model):
    recept = models.ForeignKey('Recept', on_delete=None)
    olaj = models.ForeignKey('Olaj', on_delete=None)
    mennyiseg = models.CharField(max_length=200)
    def __str__(self):
        return self.olaj.name +": "+ self.mennyiseg

