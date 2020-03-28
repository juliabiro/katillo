from django.shortcuts import render, redirect
from .models import Olaj, Recept, Forgalmazo, Forgalmazas, Hozzavalo, Hatas

# Create your views here.

def olaj(request, pk):
    if request.user.is_authenticated:
        olaj = Olaj.objects.get(pk=pk)
        hozzavalok = Hozzavalo.objects.filter(olaj__id=pk)
        receptek = set()

        # I'm sure there is a more elegant way to do this, but i can fix that later
        for h in hozzavalok:
            for r in Recept.objects.filter(pk=h.recept.id):
                receptek.add(r)
        forgalmazok = Forgalmazas.objects.filter(olaj__id=pk)

        return render(request, 'book/olaj.html', {'olaj': olaj,
                                                'receptek': receptek,
                                                'forgalmazok': forgalmazok})
    else:
        return redirect('/admin/login')

def recept(request, pk):
    if request.user.is_authenticated:
        recept = Recept.objects.get(pk=pk)
        hozzavalok = Hozzavalo.objects.filter(recept__id=pk)
        hatasok = Hatas.objects.filter(recept__id=pk)
        print(hatasok)
        return render(request, 'book/recept.html', {'recept': recept, 'hatasok': hatasok, 'hozzavalok':hozzavalok})
    else:
        return redirect('/admin/login')

def forgalmazo(request, pk):
    if request.user.is_authenticated:
        forgalmazo = Forgalmazo.objects.get(pk=pk)
        termekek = Forgalmazas.objects.filter(ceg__id=pk)
        return render(request, 'book/forgalmazo.html', {'forgalmazo':forgalmazo, 'termekek': termekek})
    else:
        return redirect('/admin/login')

def olaj_list(request):
    if request.user.is_authenticated:
        olaj_list = Olaj.objects.all()
        return render(request, 'book/olaj_list.html', {'data': olaj_list})
    else:
        return redirect('/admin/login')

def recept_list(request):
    if request.user.is_authenticated:
        recept_list = Recept.objects.all()
        return render(request, 'book/recept_list.html', {'data': recept_list})
    else:
        return redirect('/admin/login')

def arak_list(request):
    if request.user.is_authenticated:
        arak_list = Forgalmazas.objects.all()
        return render(request, 'book/arak_list.html', {'data': arak_list})
    else:
        return redirect('/admin/login')

def index(request):
    if request.user.is_authenticated:
        return render(request, 'book/index.html', {})
    else:
        return redirect('/admin/login')
