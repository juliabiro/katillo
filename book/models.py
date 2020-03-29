from django.db import models

# Create your models here.
TIPUSOK = (('1','Növényi Olaj'),('2','Hidralátum'),('3','Kometikai alapanyag'),('4',''))
MERTEKEGYSEG=(('1', 'ml'), ('2','g'), ('3', 'csepp'))

class Forgalmazo(models.Model):
    name = models.CharField(max_length=200, verbose_name='Név')
    cim = models.CharField(max_length=200, blank=True, verbose_name='Cím')
    webpage = models.CharField(max_length=200, blank=True)
    telefon = models.CharField(max_length=200, blank=True)
    class Meta:
            verbose_name_plural = 'Cégek'
            verbose_name = 'Cég'
    def __str__(self):
        return self.name

class Forgalmazas(models.Model):
    olaj = models.ForeignKey('Olaj', on_delete=None, verbose_name='Összetevő')
    termeknev = models.CharField(max_length=200, verbose_name='Terméknév')
    ceg = models.ForeignKey('Forgalmazo', on_delete=None, verbose_name='Cég')
    ar = models.IntegerField(verbose_name='Ár')
    kiszereles = models.CharField(max_length=200, verbose_name='Kiszerelés')
    mertekegyseg = models.CharField(max_length=2, choices=MERTEKEGYSEG, default='1', verbose_name='Mértékegység')
    cseppszam=models.IntegerField(blank=True, null=True, verbose_name='Cseppszám')
    tipus = models.CharField(max_length=2,
                            choices=TIPUSOK,
                             default='1', verbose_name='Típus')
    class Meta:
            verbose_name_plural = 'Termékek'
            verbose_name = 'Termék'
    def __str__(self):
        return self.termeknev+": "+ self.kiszereles

class Kontraindikacio(models.Model):
    nev = models.CharField(max_length=200)
    olaj = models.ForeignKey('Olaj', on_delete=None)

    class Meta:
            verbose_name_plural = 'Kontraindikációk'
            verbose_name = 'Kontraindikáció'

    def __str__(self):
        return self.nev

class Olaj(models.Model):
    magyar_nev = models.CharField(max_length=200, verbose_name='Magyar név')
    latin_nev = models.CharField(max_length=200, blank=True, verbose_name='Latin név')
    kep = models.CharField(max_length=200, blank=True)
    mese = models.TextField()
    fajsuj = models.IntegerField(blank=True, null=True, verbose_name='Fajsúj')
    tipus = models.CharField(max_length=2,
                            choices=TIPUSOK,
                            default='1', verbose_name='Típus')
    JEGYEK = (('1','FEJJEGY'),('2','SZIVJEGY'),('3','Alapillat'))
    jegy = models.CharField(max_length=2, choices=JEGYEK, blank=True)
    class Meta:
            verbose_name_plural = 'Összetevők'
            verbose_name = 'Összetevő'

    def __str__(self):
        return self.magyar_nev


class Recept(models.Model):
    name = models.CharField(max_length=200, verbose_name='Név')
    notes = models.TextField(verbose_name='Jegyzetek')
    TIPUSOK = (('1', 'Kozmetikum'), ('2', 'Aromaterápia'))
    tipus = models.CharField(max_length=2, default='2', choices=TIPUSOK, verbose_name='Típus')
    hatas = models.TextField(blank=True, verbose_name='Hatás')
    class Meta:
            verbose_name_plural = 'Receptek'
    def __str__(self):
        return self.name

class Hatas(models.Model):
    KOROSZTALYOK=(('1','1-3'), ( '2', '3-6'), ( '3','6-12' ), ( '4', 'felnőtt' ), ( '5','váarndós' ))
    name = models.CharField(max_length=200, verbose_name='Hatás')
    celcsoport =models.CharField(max_length=2,
                            choices=KOROSZTALYOK,
                                 default='4', verbose_name='Célcsoport')
    megjegyzesek = models.TextField(verbose_name='Megjegyzések')
    olaj = models.ForeignKey('Olaj', on_delete=None)
    def __str__(self):
        return self.name +":"+ self.celcsoport
    class Meta:
            verbose_name_plural = 'Hatások'

class Hozzavalo(models.Model):
    recept = models.ForeignKey('Recept', on_delete=None)
    olaj = models.ForeignKey('Olaj', on_delete=None, verbose_name='Összetevő')
    mennyiseg = models.CharField(max_length=200, verbose_name='mennyiség')
    mertekegyseg = models.CharField(max_length=2, choices=MERTEKEGYSEG, default='1')
    def __str__(self):
        return self.olaj.magyar_nev +": "+ self.mennyiseg+self.mertekegyseg

