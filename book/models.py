from django.db import models

# Create your models here.
TIPUSOK = (('Növényi Olaj','Növényi Olaj'),('Hidralátum','Hidralátum'),('Kometikai alapanyag','Kometikai alapanyag'),('',''))
MERTEKEGYSEG=(('ml', 'ml'), ('g','g'), ('csepp', 'csepp'))
KOROSZTALYOK=(('1-3','1-3'), ( '3-6', '3-6'), ( '6-12','6-12' ), ( 'felnőtt', 'felnőtt' ), ( 'várandós','várandós' ))

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
    mertekegyseg = models.CharField(max_length=40, choices=MERTEKEGYSEG, default='1', verbose_name='Mértékegység')
    cseppszam=models.IntegerField(blank=True, null=True, verbose_name='Cseppszám')
    tipus = models.CharField(max_length=40,
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

class Kemia_focsoport(models.Model):
    nev = models.CharField(max_length=200, verbose_name='Név')

    class Meta:
        verbose_name = 'Kémia főcsoport'
        verbose_name_plural = 'Kémia főcsoportok'

    def __str__(self):
        return self.nev

class Kemia_alcsoport(models.Model):
    nev = models.CharField(max_length=200, verbose_name='Név')

    focsoport = models.ForeignKey('Kemia_focsoport', on_delete=None, verbose_name='Kémia főcsoport', default=None)


    class Meta:
        verbose_name = 'Kémia alcsoport'
        verbose_name_plural = 'Kémia alcsoportok'

    def _focsoport(self):
        return self.focsoport.nev
    def __str__(self):
        return self._focsoport()+':'+self.nev

class Kemia(models.Model):
    alcsoport = models.ForeignKey('Kemia_alcsoport', on_delete=None, verbose_name='Kémia')
    olaj = models.ForeignKey('Olaj', on_delete=None)
    szazalek = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Kémia'
        verbose_name_plural = 'Kémia'

class AltalanosTulajdonsagFajta(models.Model):
    nev = models.CharField(max_length=200, verbose_name='Név')
    mese = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Áltlalános tulajdonság fajta'
        verbose_name_plural = 'Általános tulajdonság fajták'
    def __str__(self):
        return self.nev

class AltalanosTulajdonsag(models.Model):
    alttul = models.ForeignKey('AltalanosTulajdonsagFajta', on_delete=None, verbose_name = 'Általános tulajdonság')
    erosseg = models.IntegerField(verbose_name='erősség')
    olaj = models.ForeignKey('Olaj', on_delete=None)

class TerapiasJavaslatFajta(models.Model):
    nev = models.CharField(max_length=200, verbose_name='Név')
    mese = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Terápiás javaslat fajta'
        verbose_name_plural = 'Terápiás javaslat fajták'
    def __str__(self):
        return self.nev

class TerapiasJavaslat(models.Model):
    terjav = models.ForeignKey('TerapiasJavaslatFajta', on_delete=None, verbose_name='Terápiás Javaslat')
    erosseg = models.IntegerField(verbose_name='erősség')
    olaj = models.ForeignKey('Olaj', on_delete=None)
    class Meta:
        verbose_name = 'Terápiás javaslat'
        verbose_name_plural = 'Terápiás javaslatok'

class Hatas(models.Model):
    name = models.CharField(max_length=200, verbose_name='Hatás')
    celcsoport =models.CharField(max_length=20,
                            choices=KOROSZTALYOK,
                                 default='4', verbose_name='Célcsoport')
    megjegyzesek = models.TextField(verbose_name='Megjegyzések')
    olaj = models.ForeignKey('Olaj', on_delete=None)
    def __str__(self):
        return self.name +":"+ self.celcsoport
    class Meta:
            verbose_name = 'Összetevő Hatás'
            verbose_name_plural = 'Összetevő Hatások'


class Olaj(models.Model):
    magyar_nev = models.CharField(max_length=200, verbose_name='Magyar név')
    latin_nev = models.CharField(max_length=200, blank=True, verbose_name='Latin név')
    kep = models.CharField(max_length=200, blank=True)
    mese = models.TextField()
    fajsuj = models.FloatField(blank=True, null=True, verbose_name='Fajsúly')
    tipus = models.CharField(max_length=40,
                            choices=TIPUSOK,
                            default='1', verbose_name='Típus')
    JEGYEK = (('FEJJEGY','FEJJEGY'),('SZÍVJEGY','SZIVJEGY'),('Alapillat','Alapillat'))
    jegy = models.CharField(max_length=10, choices=JEGYEK, blank=True)

    class Meta:
            verbose_name_plural = 'Összetevők'
            verbose_name = 'Összetevő'

    def __str__(self):
        return self.magyar_nev


class Recept(models.Model):
    name = models.CharField(max_length=200, verbose_name='Név')
    notes = models.TextField(verbose_name='Jegyzetek')
    TIPUSOK = (('Kozmetikum', 'Kozmetikum'), ('Aromaterápia', 'Aromaterápia'))
    tipus = models.CharField(max_length=20, default='2', choices=TIPUSOK, verbose_name='Típus')
    hatas = models.TextField(blank=True, verbose_name='Hatás')
    class Meta:
            verbose_name_plural = 'Receptek'
    def __str__(self):
        return self.name

class Hozzavalo(models.Model):
    recept = models.ForeignKey('Recept', on_delete=None)
    olaj = models.ForeignKey('Olaj', on_delete=None, verbose_name='Összetevő')
    mennyiseg = models.CharField(max_length=200, verbose_name='mennyiség')
    mertekegyseg = models.CharField(max_length=20, choices=MERTEKEGYSEG, default='1')
    def __str__(self):
        return self.olaj.magyar_nev +": "+ self.mennyiseg+self.mertekegyseg

