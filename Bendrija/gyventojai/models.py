from django.db import models

# Create your models here.
class Gyventojas(models.Model):
    vardas = models.CharField(max_length=50)
    pavarde = models.CharField(max_length=50)
    buto_namo_nr = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    def __str__(self):
        return f"{self.vardas} {self.pavarde}"


class Butas(models.Model):
    buto_namo_nr = models.IntegerField()
    plotas = models.IntegerField()
    gyventojas = models.ForeignKey(
        Gyventojas,
        on_delete= models.CASCADE,
    )