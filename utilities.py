# Date: 26/10/2024
 
from config import MESES



def formatear_numero(numero):
    """ Formatea el número para dejarlo bonico """
    numero_str = str(numero)
    if len(numero_str) > 4:
        # Formatea el número con puntos como separadores de miles
        # Usamos el separador ',' para los miles y luego lo cambiamos por '.'.
        return f"{int(numero):,}".replace(",", ".")
    else:
        # Si tiene 4 o menos dígitos, devuélvelo tal cual
        return numero_str



def formatear_fecha(fecha):
    """ Convierte una fecha de tipo datetime.date o datetime.datetime al formato: "5 de Noviembre de 2024". """
    dia = fecha.day
    mes = MESES[fecha.month]
    year = fecha.year
    return f"{dia} de {mes} de {year}"