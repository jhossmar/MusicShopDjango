from django.db import models
from django.conf import settings
from .validators import validar_numero_caracteres_7
from .validators import validar_numero_caracteres_8
from .validators import validar_positivo
from .validators import validar_codigo_texto
from .validators import validar_fecha

class Seccion(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre

class ProductUnits(models.TextChoices):
    LIBRAS = 'lb', 'libras'
    KG = 'kg', 'Kilogramos'

class Instrument (models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    descripcion = models.TextField()
    codigo = models.SlugField(validators=[validar_numero_caracteres_7,])
    precio = models.DecimalField(decimal_places=2,max_digits=10,validators=[validar_positivo,])
    disponible = models.BooleanField(blank=True,default=True)
    peso = models.DecimalField(decimal_places=2,max_digits=10)
    unidades_peso = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.KG
    )
    
    def __str__(self):
        return self.nombre

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TextosInstrumento(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    autor = models.CharField(max_length=100,unique=False)
    editorial = models.CharField(max_length=100,unique=False)
    edicion = models.CharField(max_length=100,unique=False)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    codigo = models.SlugField(validators=[validar_numero_caracteres_8,validar_codigo_texto])
    disponible = models.BooleanField(blank=True,default=True)
    precio = models.DecimalField(decimal_places=2,max_digits=10,validators=[validar_positivo,])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class EstadoOrden(models.TextChoices):
    NOPAGADO = 'nopagado', 'No Pagado'
    PAGADO = 'pagado', 'Pagado'

class Orden(models.Model):
    fecha = models.DateField(unique='False',validators=[validar_fecha,])
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_orden_vendedor"
    )
    estado = models.CharField(
        max_length=10,
        choices=EstadoOrden.choices,
        default=EstadoOrden.NOPAGADO
    )

    def __str__(self):
        return str(self.fecha)

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE) 
    producto = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    texto = models.ForeignKey(TextosInstrumento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0,validators=[validar_positivo,])
    precio = models.DecimalField(decimal_places=2, max_digits=10,validators=[validar_positivo,])

    def __str__(self):
        return str(self.orden.fecha)

