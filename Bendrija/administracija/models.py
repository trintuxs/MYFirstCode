from django.db import models

from gyventojai.models import Butas, Gyventojas


# Create your models here.
class Balsavimas(models.Model):
    pavadinimas = models.CharField(max_length=255)
    aprasymas = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    butas = models.ForeignKey(Butas, on_delete=models.CASCADE)

    def __str__(self):
        return self.pavadinimas


class Biudziatas(models.Model):
    gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
    imoka = models