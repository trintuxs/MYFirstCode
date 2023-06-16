from django.contrib.auth.models import User
from django.db import models

from gyventojai.models import Butas, Gyventojas


# Create your models here.
class Balsavimas(models.Model):
    pavadinimas = models.CharField(max_length=255)
    aprasymas = models.TextField()
    balsas = models.ForeignKey(Butas, on_delete=models.CASCADE)

    data = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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


class Biudziatas(models.Model):
      gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
      imoka = models.FloatField()

      data = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
          return f"{self.gyventojas} {self.imoka}"

      class Meta:
          verbose_name = 'Biudziatas'
          verbose_name_plural = 'Biudziatas'


class Inasas(models.Model):
     gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
     suma = models.FloatField()

     data = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     def __str__(self):
         return f"{self.gyventojas} {self.suma}"

     class Meta:
         verbose_name = 'Inasas'
         verbose_name_plural = 'Inasas'

class Islaidos(models.Model):
     panaudota = models.TextField()
     suma = models.FloatField()
     mokestis = models.FloatField()
     data = models.DateTimeField(auto_now_add=True)


     def __str__(self):
         return f"{self.mokestis} {self.suma}"

     class Meta:
         verbose_name = 'Islaidos'
         verbose_name_plural = 'Islaidos'
