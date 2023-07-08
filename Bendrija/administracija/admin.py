from django.contrib import admin

from administracija.models import Balsavimas, Diskusija,  Islaidos, Balansas, Vadovybe, Kaupiamasis_Inasas, Mokesciai

# Register your models here.

admin.site.register(Balsavimas)
admin.site.register(Diskusija)
admin.site.register(Balansas)
admin.site.register(Islaidos)
admin.site.register(Vadovybe)
admin.site.register(Kaupiamasis_Inasas)
admin.site.register(Mokesciai)