from django.contrib import admin

from administracija.models import Balsavimas, Diskusija,  Islaidos, Balansas

# Register your models here.

admin.site.register(Balsavimas)
admin.site.register(Diskusija)
admin.site.register(Balansas)
admin.site.register(Islaidos)