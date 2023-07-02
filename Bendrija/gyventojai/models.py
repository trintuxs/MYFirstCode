from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Gyventojas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vardas = models.CharField(max_length=50, verbose_name="Vardas")
    pavarde = models.CharField(max_length=50, verbose_name="Pavardė")
    email = models.CharField(max_length=50, verbose_name="Elektroninis paštas")
    butas_namas = models.ForeignKey('Butas',on_delete=models.SET_NULL, null=True, related_name='savininkas')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

    class Meta:
        verbose_name = 'Gyventojas'
        verbose_name_plural = 'Gyventojas'



class Butas(models.Model):
    buto_namo_nr = models.IntegerField()
    plotas_kv = models.IntegerField()

    class Meta:
        verbose_name = 'Butas'
        verbose_name_plural = 'Butas'


class Vadovybe(models.Model):
    darbuotojas = models.ForeignKey(User, on_delete=models.CASCADE)
    vardas = models.CharField(max_length=70, verbose_name="Vardas")
    pavarde = models.CharField(max_length=70, verbose_name="Pavarde")
    pareigos = models.CharField(max_length=120,  verbose_name="Pareigos")
    atliginimas = models.IntegerField( verbose_name="Atliginimas")
    darbai = models.IntegerField(verbose_name="Islaidos uz darbus")

