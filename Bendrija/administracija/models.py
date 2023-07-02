from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from gyventojai.models import Butas, Gyventojas, Vadovybe


# Create your models here.
class Balsavimas(models.Model):
    pavadinimas = models.CharField(max_length=255)
    aprasymas = models.TextField()
    balsas = models.ForeignKey(Butas, on_delete=models.CASCADE)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pavadinimas
    class Meta:
        verbose_name = 'Balsavimas'
        verbose_name_plural = 'Balsavimas'


class Diskusija(models.Model):
    pavadinimas = models.CharField(max_length=100)
    aprasymas = models.TextField()
    autorius = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.pavadinimas} {self.aprasymas} {self.autorius}"

    class Meta:
        verbose_name = 'Diskusija'
        verbose_name_plural = 'Diskusija'





class Inasas(models.Model):
     gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
     suma = models.FloatField()
     data = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return f"Inasas: {self.gyventojas} - {self.suma}"

     class Meta:
         verbose_name = 'Inasas'
         verbose_name_plural = 'Inasai'

class Islaidos(models.Model):
     administracija = models.ForeignKey(Vadovybe, on_delete=models.CASCADE)
     panaudota = models.TextField()
     suma = models.FloatField()
     mokestis = models.FloatField()
     data = models.DateTimeField(auto_now_add=True)


     def __str__(self):
         return f"Islaidos {self.administracija} - {self.suma}"


#gaunama informacija is Vadovybes klases
     def save(self, *args, **kwargs):
         vadovybe = self.administracija
         atliginimas = vadovybe.atliginimas
         darbai = vadovybe.darbai
#apskaiciuojama suma
         self.suma = atliginimas + darbai
         super().save(*args, **kwargs)

     class Meta:
         verbose_name = 'Islaidos'
         verbose_name_plural = 'Islaidos'


class Balansas(models.Model):
    gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
    inaso_suma = models.FloatField(default=0)
    islaidu_suma = models.FloatField(default=0)
    atnaujinimo_data = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Balansas: {self.gyventojas}"

    class Meta:
        verbose_name = 'Balansas'
        verbose_name_plural = 'Balansai'

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.atnaujinimo_data = datetime.now().date()  # Nustatyti atnaujinimo datą naujam įrašui

        super().save(*args, **kwargs)

#uzklausa kuri gauna visus Inasus susijusius su tam tikru gyventoju, aggregate  grazina bendra suma
    def apskaiciuoti_inesama_suma(self):
        self.inaso_suma = Inasas.objects.filter(gyventojas=self.gyventojas).aggregate(models.Sum('suma'))['suma__sum'] or 0
        self.save()

    def apskaiciuoti_islaidu_suma(self):
        self.islaidu_suma = Islaidos.objects.filter(gyventojas=self.gyventojas).aggregate(models.Sum('suma'))['suma__sum'] or 0
        self.save()
