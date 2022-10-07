from rest_framework import serializers
from .models import Instrument
from .models import Seccion
from .models import TextosInstrumento
from .models import OrdenProducto



class InstrumentSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = "__all__"

class SeccionSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = "__all__"

class TextosInstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextosInstrumento
        fields = "__all__"

class OrdenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProducto
        fields = "__all__"

class ReporteSerializer(serializers.Serializer):
    numero_instrumentos= serializers.IntegerField()
    numero_textos = serializers.IntegerField()
    instrumentos = InstrumentSerialiazer(many=True)
    textos = TextosInstrumentoSerializer(many=True)
