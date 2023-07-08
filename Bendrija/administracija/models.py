
from django.contrib.auth.models import User
from datetime import date
from django.db import models

from gyventojai.models import Butas, Gyventojas


# Create your models here.

class Vadovybe(models.Model):
    darbuotojas = models.ForeignKey(User, on_delete=models.CASCADE)
    vardas = models.CharField(max_length=70, verbose_name="Vardas")
    pavarde = models.CharField(max_length=70, verbose_name="Pavarde")
    pareigos = models.CharField(max_length=120,  verbose_name="Pareigos")
    atliginimas = models.IntegerField( verbose_name="Atliginimas")

    def skaiciuoti_atlyginima(self):
            mokesciai = Mokesciai.objects.filter(gyventojas__butas_namas__savininkas=self)
            suma_mokesciu = 0
            for mokestis in mokesciai:
                suma_mokesciu += mokestis.gyventojas.butas_namas.plotas_kv * 0.15

            ataskaita = Mokesciai.objects.create(gyventojas=self, apmoketi=False)
            ataskaita.save()

            return suma_mokesciu
    class Meta:
        verbose_name = 'Vadovybė'
        verbose_name_plural = 'Vadovybė'  

    



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



#kaupiamojo inaso suskaiciavimas

class Kaupiamasis_Inasas(models.Model):
     gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
     suma = models.FloatField()
     data = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return f"Kaupiamasis Inasas: {self.gyventojas} - {self.suma}"

     class Meta:
         verbose_name = 'Kaupiamsis nasas'
         verbose_name_plural = 'Kaupiamieji Inasai'

def apskaiciuoti_inaso_suma(self):
    suma = 0
    kaupiamieji_inasai = Kaupiamasis_Inasas.objects.filter(gyventojas=self)
    for inasas in kaupiamieji_inasai:
        suma += inasas.suma
    self.balansas.inaso_suma = suma
    self.balansas.balanso_atnaujinimo_data = date.today()
    self.balansas.save()

    # Atnaujinti balansą, jei praėjo 2 dienos po paskutinio atnaujinimo
    if (date.today() - self.balansas.balanso_atnaujinimo_data).days >= 2:
        self.atnaujinti_balansa()

def atnaujinti_balansa(self):
    islaidos = Islaidos.objects.filter(administracija=self)
    suma_islaidu = 0
    for islaida in islaidos:
        suma_islaidu += islaida.suma
    self.balansas.inaso_suma -= suma_islaidu
    self.balansas.save()

#mokescio apskaiciavimas pagal kvadratura

class Mokesciai(models.Model):
    gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
    apmoketi = models.BooleanField(default=False)

    def paskaiciavimas(self):
        butai = Butas.objects.all()
        for butas in butai:
            moketina_suma = butas.plotas_kv * 0.15
            savininkai = Gyventojas.objects.filter(butas_namas=butas)
            for savininkas in savininkai:
                Mokesciai.objects.create(gyventojas=savininkas, apmoketi=False, moketina_suma=moketina_suma )



class Islaidos(models.Model):
     administracija = models.ForeignKey(Vadovybe, on_delete=models.CASCADE)
     panaudota = models.TextField()
     suma = models.FloatField()
     data = models.DateTimeField(auto_now_add=True)
     iskaičiuota = models.BooleanField(default=False)

     def __str__(self):
         return f"Islaidos {self.administracija} - {self.suma}"

     def save(self, *args, **kwargs):
         vadovybe = self.administracija
         atliginimas = vadovybe.atliginimas

         self.suma = atliginimas
         super().save(*args, **kwargs)

         gyventojas = self.administracija.darbuotojas
         balansas = Balansas.objects.get(gyventojas=gyventojas)
         balansas.inaso_suma -= self.suma
         balansas.save()

     class Meta:
         verbose_name = 'Islaidos'
         verbose_name_plural = 'Islaidos'


class Balansas(models.Model):
    gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
    inaso_suma = models.FloatField(default=0)
    balanso_atnaujinimo_data = models.DateField(auto_now_add=True)
   
    atnaujinimo_data = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Balansas: {self.gyventojas}"

    class Meta:
        verbose_name = 'Balansas'
        verbose_name_plural = 'Balansai'
