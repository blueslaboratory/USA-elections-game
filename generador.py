# Date: 23/12/2024

import os
import json
import random
from datetime import datetime, timedelta
from config import fecha_inicial, fecha_final, output_folder, estados, sexo, religiones, etnias, estudios
from config import pesos_votos, modelo_democrata, modelo_republicano
from config import TURNOS_TOTALES 



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

    # Cada turno avanza intervalo_dias
    intervalo_dias = ((fecha_final - fecha_inicial).days) // (TURNOS_TOTALES - 1)
    # print("intervalo_dias:", intervalo_dias)

    inicio_turno = fecha_inicial + timedelta(days=intervalo_dias * (turno - 1))
    fin_turno = min(inicio_turno + timedelta(days=intervalo_dias), fecha_final + timedelta(hours=23, minutes=59, seconds=59))
    # print("inicio_turno:", inicio_turno.date(), "fin_turno:", fin_turno.date())

    # Crear el directorio del jugador
    jugador_folder = os.path.join(output_folder, f"jugador_{jugador.strip().lower()}")
    os.makedirs(jugador_folder, exist_ok=True)


    for i in range(num_votantes):
        
        fecha_voto_random = (inicio_turno + timedelta(seconds=random.randint(0, (fin_turno - inicio_turno).total_seconds())))
        
        # Asegurar que no exceda la fecha final
        if fecha_voto_random > fecha_final: 
            fecha_voto_random = fecha_final

        fecha_voto_random = fecha_voto_random.strftime("%Y-%m-%d")
        # print("fecha_voto_random:", fecha_voto_random)

        votante = {
            # ID único del votante
            # id = 249: [0, 1999], e.g. 249+1 +(turno=1 -1)*250 = 250
            "id": i+1 + (turno-1)*num_votantes,

            # Fecha de voto con variación aleatoria dentro del mes
            "fecha_voto": fecha_voto_random,

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