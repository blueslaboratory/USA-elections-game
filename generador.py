# Date: 23/12/2024

import os
import json
import random
from datetime import datetime, timedelta
from config import fecha_inicial, output_folder, estados, sexo, religiones, etnias, estudios
from config import pesos_votos, modelo_democrata, modelo_republicano


# Crear carpetas para guardar datos:
os.makedirs(output_folder, exist_ok=True)


# Funcion para calcular el voto basado en los modelos:
def calcular_voto(votante, pesos):
    """Fórmula para calcular la probabilidad de que un votante sea democrata o republicano"""

    probabilidad_democrata = (
        pesos["estado"] * (1 if votante["estado"] in modelo_democrata["estado"] else 0) +
        pesos["estudios"] * (1 if votante["estudios"] in modelo_democrata["estudios"] else 0) +
        pesos["etnia"] * (1 if votante["etnia"] in modelo_democrata["etnia"] else 0) +
        pesos["edad"] * (1 if votante["edad"] in modelo_democrata["edad"] else 0) +
        pesos["sexo"] * (1 if votante["sexo"] in modelo_democrata["sexo"] else 0) +
        # si el salario esta dentro del rango: salario[0] <= salario <= salario[1]
        pesos["salario"] * (1 if modelo_democrata["salario"][0] <= votante["salario"] <= modelo_democrata["salario"][1] else 0) +
        pesos["religion"] * (1 if votante["religion"] in modelo_democrata["religion"] else 0)
    )

    probabilidad_republicano = (
        pesos["estado"] * (1 if votante["estado"] in modelo_republicano["estado"] else 0) +
        pesos["estudios"] * (1 if votante["estudios"] in modelo_republicano["estudios"] else 0) +
        pesos["etnia"] * (1 if votante["etnia"] in modelo_republicano["etnia"] else 0) +
        pesos["edad"] * (1 if votante["edad"] in modelo_republicano["edad"] else 0) +
        pesos["sexo"] * (1 if votante["sexo"] in modelo_republicano["sexo"] else 0) +
        # si el salario esta dentro del rango: salario[0] <= salario <= salario[1]
        pesos["salario"] * (1 if modelo_republicano["salario"][0] <= votante["salario"] <= modelo_republicano["salario"][1] else 0) +
        pesos["religion"] * (1 if votante["religion"] in modelo_republicano["religion"] else 0)
    )

    # Decidir voto
    if probabilidad_democrata > probabilidad_republicano:
        return "democrata"
    elif probabilidad_republicano > probabilidad_democrata:
        return "republicano"
    # Empate
    else:
        return random.choice(["democrata", "republicano"])



# Generar votantes:
def generar_votantes(turno, jugador, num_votantes=250, impacto=None):
    """Generar votantes con opción de aplicar impacto específico."""

    votantes = []

    # Cada turno avanza 30 dias
    fecha_voto = fecha_inicial + timedelta(days=(turno - 1) * 30)

    # Crear el directorio del jugador
    jugador_folder = os.path.join(output_folder, f"jugador_{jugador.strip().lower()}")
    os.makedirs(jugador_folder, exist_ok=True)


    for i in range(num_votantes):

        votante = {
            # ID único del votante
            # id = 249: [0, 1999], e.g. 249+1 +(turno=1 -1)*250 = 250
            "id": i+1 + (turno-1)*num_votantes,

            # Fecha de voto con variación aleatoria dentro del mes
            # 30dias * 24h * 60min * 60s = 2592000s
            "fecha_voto": (fecha_voto + timedelta(seconds=random.randint(0, 30*24*60*60))).strftime("%Y-%m-%d"),

            # Atributos del votante generados aleatoriamente o basados en impacto
            "estado": random.choice(impacto["estado"] if impacto and "estado" in impacto else estados),
            "etnia": random.choice(impacto["etnia"] if impacto and "etnia" in impacto else etnias),
            "edad": random.choice(impacto["edad"] if impacto and "edad" in impacto else range(18, 99)),
            "sexo": random.choice(impacto["sexo"] if impacto and "sexo" in impacto else sexo),
            "salario": random.randint(min(impacto["salario"]), max(impacto["salario"])) if impacto and "salario" in impacto else random.randint(30 * 1000, 250 * 1000),
            "estudios": random.choice(impacto["estudios"] if impacto and "estudios" in impacto else estudios),
            "religion": random.choice(impacto["religion"] if impacto and "religion" in impacto else religiones),

            # Atributos generados aleatoriamente (no han sido parametrizados para tener impacto)
            "casado": random.choice([True, False]),
            "hijos": random.randint(0, 5)
        }

        # Calcular el voto basado en los modelos y pesos
        votante["voto"] = calcular_voto(votante, pesos_votos)

        # Agregar el votante a la lista
        votantes.append(votante)

        # Guardar cada votante como archivo JSON
        with open(os.path.join(jugador_folder, f"votante_{votante['id']}.json"), "w") as f:
            json.dump(votante, f, indent=4)

    return votantes
