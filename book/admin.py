from django.contrib import admin
from .models import *

class BeszerzesAdminSite(admin.AdminSite):
    site_header = "Beszerzési admin"
    site_title = "Beszerzési admin"
    index_title = "Beszerzési admin"

beszerzes_admin = BeszerzesAdminSite(name='beszerzes_admin')

class TudasAdminSite(admin.AdminSite):
    site_header = "Tudás admin"
    site_title = "Tudás admin"
    index_title = "Tudás admin"

tudas_admin = TudasAdminSite(name='tudas_admin')

class ReceptAdminSite(admin.AdminSite):
    site_header = "Recept admin"
    site_title = "Recept admin"
    index_title = "Recept admin"

recept_admin = TudasAdminSite(name='recept_admin')



class ForgalmazasAdmin(admin.TabularInline):
    model = Forgalmazas
    fk_name = 'olaj'
    extra=0

class TermekAdmin(admin.TabularInline):
    model = Forgalmazas
    fk_name = 'ceg'
    extra=0

class ForgalmazoAdmin(admin.ModelAdmin):
    inlines = [TermekAdmin]

class HozzavaloAdmin(admin.TabularInline):
    model = Hozzavalo
    fk_name = 'recept'
    extra=0

class ReceptAdmin(admin.ModelAdmin):
    inlines = [HozzavaloAdmin]

class HatasAdmin(admin.TabularInline):
    model = Hatas
    fk_name = 'olaj'
    extra=0

class KemiaAdmin(admin.TabularInline):
    model = Kemia
    fk_name = 'olaj'
    extra=0

class TulajdonsagAdmin(admin.TabularInline):
    model = AltalanosTulajdonsag
    fk_name='olaj'
    extra=0

class TerapiasJavaslatAdmin(admin.TabularInline):
    model = TerapiasJavaslat
    fk_name='olaj'
    extra=0

class OlajAdmin(admin.ModelAdmin):
    inlines = [KemiaAdmin, TulajdonsagAdmin, TerapiasJavaslatAdmin, HatasAdmin, ForgalmazasAdmin]

# Register your models here.
beszerzes_admin.register(Forgalmazo, ForgalmazoAdmin)
beszerzes_admin.register(Forgalmazas)
tudas_admin.register(Kemia_focsoport)
tudas_admin.register(Kemia_alcsoport)
tudas_admin.register(AltalanosTulajdonsagFajta)
tudas_admin.register(TerapiasJavaslatFajta)
recept_admin.register(Olaj, OlajAdmin)
recept_admin.register(Recept, ReceptAdmin)


