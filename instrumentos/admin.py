from django.contrib import admin
from .models import Seccion
from .models import Instrument
from .models import TextosInstrumento
from .models import OrdenProducto
from .models import Orden


admin.site.register(Seccion)

class InstrumentAdmin (admin.ModelAdmin):
    list_display = ("nombre","seccion","precio","codigo","peso","unidades_peso","disponible")
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible",)

admin.site.register(Instrument,InstrumentAdmin)

class TextosInstrumentoAdmin (admin.ModelAdmin):
    list_display = ("nombre","autor","editorial","seccion","codigo","precio","disponible")
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible",)
admin.site.register(TextosInstrumento,TextosInstrumentoAdmin)
admin.site.register(OrdenProducto)
admin.site.register(Orden)
# Register your models here.
