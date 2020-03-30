from django.contrib import admin
from .models import *

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
admin.site.register(Forgalmazo, ForgalmazoAdmin)
admin.site.register(Olaj, OlajAdmin)
admin.site.register(Recept, ReceptAdmin)
admin.site.register(Forgalmazas)
admin.site.register(Hatas)
admin.site.register(Kemia_focsoport)
admin.site.register(Kemia_alcsoport)
admin.site.register(AltalanosTulajdonsagFajta)
admin.site.register(TerapiasJavaslatFajta)


