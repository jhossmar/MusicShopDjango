from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .models import Instrument
from .serializers import InstrumentSerialiazer
from .models import Seccion
from .serializers import SeccionSerialiazer
from .models import TextosInstrumento
from .serializers import TextosInstrumentoSerializer
from .models import OrdenProducto
from .serializers import OrdenProductoSerializer
from .serializers import ReporteSerializer
VIENTOS_MADERAS=7

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerialiazer

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerialiazer

class TextosInstrumentoViewSet(viewsets.ModelViewSet):
    queryset = TextosInstrumento.objects.all()
    serializer_class = TextosInstrumentoSerializer

class OrdenCreateAndList(generics.CreateAPIView,generics.ListAPIView):
    queryset = OrdenProducto.objects.all()
    serializer_class = OrdenProductoSerializer

@api_view(["GET"])
def instrumentos_cantidad(request):
    try:
        cantidad = Instrument.objects.count()
        count_cuerdas = 0
        count_vientos_maderas=0
        count_vientos_metales=0
        count_percusion=0
        count_pianos=0
        count_accesorios=0
        count_another=0

        # print(cantidad)
        for i in range(cantidad):
            # print(i+1)
            container = Instrument.objects.get(pk=i+1)
            # print(container.seccion)
            if str(container.seccion) == 'VIENTOS_MADERAS':
                count_vientos_maderas = count_vientos_maderas+1
            elif str(container.seccion) == 'VIENTOS_METALES':
                count_vientos_metales = count_vientos_metales+1
            elif str(container.seccion) == 'CUERDAS':
                count_cuerdas = count_cuerdas+1
            elif str(container.seccion) == 'PIANOS':
                count_pianos = count_pianos+1
            elif str(container.seccion) == 'ACCESSORIOS':
                count_accesorios = count_accesorios+1
            elif str(container.seccion) == 'PERCUSION':
                count_percusion = count_percusion+1
            else:
                count_another = count_another+1
            # print(ejemplo.seccion)
            # print(i)
        
        return JsonResponse(
            {
                "vientos_maderas": count_vientos_maderas,
                "vientos_metales": count_vientos_metales,
                "cuerdas": count_cuerdas,
                "pianos": count_pianos,
                "accesorios": count_accesorios,
                "percusion": count_percusion,
                "otros": count_another
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def textos_vientos_maderas(request):
    try:
        textos = TextosInstrumento.objects.all()
        resultado=textos.filter(seccion=VIENTOS_MADERAS)
        return JsonResponse(
            TextosInstrumentoSerializer(resultado, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_general(request):
    try:
        instrumentos = Instrument.objects.all()
        textos = TextosInstrumento.objects.all()
        cantidad_instr = instrumentos.count()
        cantidad_textos = textos.count()

        return JsonResponse(
            ReporteSerializer({
                "numero_instrumentos": cantidad_instr,
                "instrumentos": instrumentos,
                "numero_textos": cantidad_textos,
                "textos": textos,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)
