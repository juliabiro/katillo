from django.shortcuts import render
from .models import Olaj, Recept, Forgalmazo, Forgalmazas, Hozzavalo

# Create your views here.

def olaj(request, pk):
    olaj = Olaj.objects.get(pk=pk)
    receptek = Recept.objects.filter(hozzavalok__olaj__id=pk)
    forgalmazok = Forgalmazas.objects.filter(olaj__id=pk) 
    return render(request, 'book/olaj.html', {'olaj': olaj,
                                              'receptek': receptek,
                                              'forgalmazok': forgalmazok})

def recept(request, pk):
    recept = Recept.objects.get(pk=pk)
    hozzavalok = recept.hozzavalok.all()
    hatasok = recept.hatasok.all()
    return render(request, 'book/recept.html', {'recept': recept, 'hatasok': hatasok, 'hozzavalok':hozzavalok})

def forgalmazo(request, pk):
    forgalmazo = Forgalmazo.objects.get(pk=pk)
    termekek = Forgalmazas.objects.filter(ceg__id=pk)
    return render(request, 'book/forgalmazo.html', {'forgalmazo':forgalmazo, 'termekek': termekek})

def olaj_list(request):
    olaj_list = Olaj.objects.all()
    return render(request, 'book/olaj_list.html', {'data': olaj_list})

def recept_list(request):
    recept_list = Recept.objects.all()
    return render(request, 'book/recept_list.html', {'data': recept_list})

def arak_list(request):
    arak_list = Forgalmazas.objects.all()
    return render(request, 'book/arak_list.html', {'data': arak_list})

def index(request):
    return render(request, 'book/index.html', {})
