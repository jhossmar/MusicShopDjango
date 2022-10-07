from django.core.exceptions import ValidationError
from datetime import date

def validar_numero_caracteres_7(value):
    if len(value)!=7:
        raise ValidationError(
            '%(value)s no es un codigo permitido',
            params = {'value':value}
        )

def validar_positivo(value):
    if float(value) <=0:
        raise ValidationError(
            '%(value)s no es un valor positivo',
            params = {'value':value}
        )

def validar_numero_caracteres_8(value):
    if len(value)!=8:
        raise ValidationError(
            '%(value)s no es un codigo permitido',
            params = {'value':value}
        )

def validar_codigo_texto(value):
    if value[3]!='T':
        raise ValidationError(
            '%(value)s no es un codigo permitido',
            params = {'value':value}
        )

def validar_fecha(value):
    actual_date = date.today()
    today = actual_date.strftime("%d")
    if int(value.strftime("%d"))<int(today):
        raise ValidationError(
            '%(value)s no es una fecha permitida',
            params = {'value':value}
        )