from django.contrib import admin

from administracija.models import Balsavimas, Diskusija, Biudziatas, Islaidos

# Register your models here.

admin.site.register(Balsavimas)
admin.site.register(Diskusija)
admin.site.register(Biudziatas)
admin.site.register(Islaidos)