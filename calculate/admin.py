from django.contrib import admin
from .models import Ciudad, Distance


class CiudadAdmin (admin.ModelAdmin):
    list_display = ('nombre', 'latitud', 'longitud')


class DistanceAdmin (admin.ModelAdmin):
    list_display = ('distancia', )


admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Distance, DistanceAdmin)
