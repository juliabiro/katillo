from django.shortcuts import render, redirect
from .models import * 

# Create your views here.

def olaj(request, pk):
    if request.user.is_authenticated:
        olaj = Olaj.objects.get(pk=pk)
        data = {
            'olaj': olaj,
            'kemia': [],
            'altalanos_tulajdonsagok': [],
            'terapias_javasatok':[],
            'hatasok':[],
            'receptek':[],
            'termekek':[],
        }

        hozzavalok = Hozzavalo.objects.filter(olaj__id=pk)
        data['termekek'] = Forgalmazas.objects.filter(olaj__id=pk)
        kemiak = Kemia.objects.filter(olaj__id=pk)
        data['kemiak'] = [{'focsoport': k.alcsoport.focsoport.nev,
                           'alcsoport': k.alcsoport.nev,
                           'szazalek': k.szazalek} for k in kemiak]
        alttul = AltalanosTulajdonsag.objects.filter(olaj__id=pk).order_by('-erosseg')
        data['altalanos_tulajdonsagok'] = [ {
            'tulajdonsag': t.alttul.nev,
            'erosseg': t.erosseg
        } for t in alttul]

        terjav = TerapiasJavaslat.objects.filter(olaj__id=pk).order_by('-erosseg')
        data['terapias_javasatok'] = [{
            'tulajdonsag': t.terjav,
            'erosseg':t.erosseg
        }for t in terjav]

        hatasok = Hatas.objects.filter(olaj__id=pk)
        data['hatasok'] =[ {
            'nev': h.name,
            'celcsoport': h.celcsoport,
            'notes': h.megjegyzesek
        } for h in hatasok]
        receptek = set()
        # I'm sure there is a more elegant way to do this, but i can fix that later
        for h in hozzavalok:
            for r in Recept.objects.filter(pk=h.recept.id):
                receptek.add(r)
        data['receptek'] = receptek

        return render(request, 'book/olaj.html', data)
    else:
        return redirect('/admin/login')

def recept(request, pk):
    if request.user.is_authenticated:
        recept = Recept.objects.get(pk=pk)
        hozzavalok = Hozzavalo.objects.filter(recept__id=pk)
        hozzavalok =[ {
            'olaj': {
                'nev': h.olaj.magyar_nev,
                'id': h.olaj.id,
            },
            'mennyiseg': h.mennyiseg,
            'mertekegyseg': h.mertekegyseg
        } for h in hozzavalok]
        return render(request, 'book/recept.html', {'recept': recept, 'hozzavalok':hozzavalok})
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
