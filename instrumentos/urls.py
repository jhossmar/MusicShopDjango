from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"instruments", views.InstrumentViewSet)
router.register(r"seccions", views.SeccionViewSet)
router.register(r"textosInstruments", views.TextosInstrumentoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('ordenes/create_list', views.OrdenCreateAndList.as_view(), name='ordens'),
    path('instrumentos/cantidad',views.instrumentos_cantidad),
    path('textos/filtrar/maderas',views.textos_vientos_maderas),
    path('reporte',views.reporte_general),
]