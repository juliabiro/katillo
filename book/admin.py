from django.contrib import admin
from .models import *

class ForgalmazasAdmin(admin.TabularInline):
    model = Forgalmazas
    fk_name = 'olaj'
    extra=0

class HatasAdmin(admin.TabularInline):
    model = Hatas
    fk_name = 'olaj'
    extra=0

class OlajAdmin(admin.ModelAdmin):
    inlines = [ForgalmazasAdmin, HatasAdmin]

class HozzavaloAdmin(admin.TabularInline):
    model = Hozzavalo
    fk_name = 'recept'
    extra=0

class ReceptAdmin(admin.ModelAdmin):
    inlines = [HozzavaloAdmin]


class TermekAdmin(admin.TabularInline):
    model = Forgalmazas
    fk_name = 'ceg'
    extra=0

class ForgalmazoAdmin(admin.ModelAdmin):
    inlines = [TermekAdmin]
# Register your models here.
admin.site.register(Forgalmazo, ForgalmazoAdmin)
admin.site.register(Olaj, OlajAdmin)
admin.site.register(Recept, ReceptAdmin)
admin.site.register(Forgalmazas)
admin.site.register(Hatas)

