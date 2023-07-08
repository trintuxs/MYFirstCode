from django.shortcuts import render
from django.views import View

from administracija.models import Vadovybe, Islaidos, Balsavimas, Diskusija
from gyventojai.models import Gyventojas


class AtaskaitaMokesciaiView(View):
    def get(self, request, pk):
        vadovybe = Vadovybe.objects.get(pk=pk)
        suma_mokesciu = vadovybe.skaiciuoti_atlyginima()
        return render(request, 'ataskaita_mokesciai.html', {'vadovybe': vadovybe, 'suma_mokesciu': suma_mokesciu})


class IslaidosView(View):
    def get(self, request, pk):
        gyventojas = Gyventojas.objects.get(pk=pk)
        islaidos = Islaidos.objects.filter(administracija=gyventojas.vadovybe)
        return render(request, 'islaidos.html', {'gyventojas': gyventojas, 'islaidos': islaidos})


class BalsavimasView(View):
    def get(self, request, pk):
        balsavimas = Balsavimas.objects.get(pk=pk)
        return render(request, 'balsavimas.html', {'balsavimas': balsavimas})


class DiskusijaView(View):
    def get(self, request, pk):
        diskusija = Diskusija.objects.get(pk=pk)
        atsakymai = diskusija.atsakymai.all()
        return render(request, 'diskusija.html', {'diskusija': diskusija, 'atsakymai': atsakymai})

class Gyventojo_inasas(View):
    def gyventojo_inasas(request, pk):
        gyventojas = Gyventojas.objects.get(pk=pk)
        return render(request, 'gyventojo_inasas.html', {'gyventojas': gyventojas})