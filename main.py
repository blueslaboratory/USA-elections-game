# Date: 23/12/2024

import time
import select
import sys
import random
# import cleanup

from acciones import accion_analisis, acciones_democratas, acciones_republicanas
from players import Player
from generador import generar_votantes
from config import TURNOS_TOTALES, MINUTOS_ANALISIS
from config import fecha_inicial, fecha_final, MESES
from utilities import formatear_fecha, formatear_numero

from collections import Counter
from datetime import datetime, timedelta




# INCIO LIMPIO: Borrar las carpetas del juego anterior
# cleanup.borrar_carpetas()




def calcular_fechas_turnos(fecha_inicial, fecha_final):
    """ Genera una lista de fechas equitativamente distribuidas entre fecha_inicial y fecha_final. """
    
    # Calcular el intervalo de días entre turnos
    intervalo_dias = (fecha_final - fecha_inicial).days // (TURNOS_TOTALES - 1)

    # Generar las fechas de los turnos
    fechas_turnos = [fecha_inicial + timedelta(days = i*intervalo_dias) for i in range(TURNOS_TOTALES)]

    # Asegurar que la última fecha no sobrepase fecha_final
    fechas_turnos[-1] = min(fechas_turnos[-1], fecha_final)

    return [fecha.date() for fecha in fechas_turnos]




def mostrar_opciones(jugador):
    """Mostrar las opciones disponibles para el jugador."""
    if jugador.name.strip().lower() == "democrata":
        return random.sample(acciones_democratas, 3) + [accion_analisis]
    else:
        return random.sample(acciones_republicanas, 3) + [accion_analisis]




def elegir_accion(jugador, acciones_turno):
    """Permitir al jugador elegir una acción."""

    # Mostrar opciones al jugador
    print("\nOpciones disponibles para la campaña:")
    for i, accion in enumerate(acciones_turno):
        # Determinar el formato del coste
        if accion['coste'] < 0:
            # Formato para costes negativos
            coste_formateado = f"(Ingreso: +{formatear_numero(abs(accion['coste']))}$)"
        else:
            # Formato para costes positivos
            coste_formateado = f"(Coste: {formatear_numero(accion['coste'])}$)"

        # Imprimir la opción con el formato adecuado
        print(f"{i + 1}. {accion['nombre']} - {coste_formateado}")

    # Capturar elección 
    jugador_elija = True
    while jugador_elija:
        
        try:
            eleccion = int(input("\nSelecciona una opción (1-4): ")) - 1
            if eleccion not in range(len(acciones_turno)):
                raise ValueError

            accion_seleccionada = acciones_turno[eleccion]

            # Verificar si tiene suficiente dinero
            if accion_seleccionada["coste"] > jugador.money:
                # Dinero insuficiente
                print(f"No tienes dinero suficiente para esta acción. Dinero actual: ${formatear_numero(jugador.money)}. \n¿Quieres pasar? (yes/no)")
                pasar = input("> ").strip().lower()
                if pasar == "yes":
                    print("Has pasado este turno.")
                    jugador_elija = False
                    return None
                else:
                    print("Selecciona otra opción.")
            else:
                # Dinero suficiente
                jugador_elija = False
                return accion_seleccionada

        except ValueError:
            print("Entrada no válida. Por favor selecciona un número entre 1 y 4.")




def ejecutar_analisis(jugador, coste):
    """Ejecutar la lógica de análisis de datos."""

    jugador.money -= coste

    print("\n¡Has elegido: Análisis! (El análisis no consume turno)")
    print("\nProcesando los datos de los votantes...")
    print(f"Tienes {MINUTOS_ANALISIS} minutos para procesar los datos con NiFi, realizar consultas en MongoDB \no consultar gráficos y estadísticas en Jupyter/Spark")
    input("\nPresiona ENTER para comenzar. Si acabas antes de tiempo vuelve a presionar ENTER...")

    try:
        for remaining in range(MINUTOS_ANALISIS*60, 0, -1):
            # Pausa de 1 segundo
            time.sleep(1)

            # Mensajes al jugador
            if remaining == MINUTOS_ANALISIS*60:
                print(f"¡Tempus Fugit! ¡Comienza la cuenta atrás! - Tiempo restante: {MINUTOS_ANALISIS} minutos")
            if remaining == 60:
                print("Tic, tac, quedan 60 segundos")
            if remaining == 1:
                print("¡Se acabó el tiempo! ¡Paren la investigación electoral!")

            # Verificar si hay entrada del usuario
            '''
            Verifica si hay entrada del usuario (sys.stdin) disponible para leer.
            Parámetros:
            [sys.stdin] -> Lista de objetos a monitorizar para lectura.
            [] -> No se monitorizan objetos para escritura.
            [] -> No se monitorizan errores.
            0 -> Timeout inmediato; no bloquea la ejecución.
            '''
            if select.select([sys.stdin], [], [], 0)[0]:
                input()  # Limpiar el buffer
                remaining = 2
                print("Análisis finalizado antes de tiempo. Continuemos.")
                break

    except KeyboardInterrupt:
        print("\nAnálisis finalizado manualmente.")

    print("Regresando al turno actual...")

    return "reanudar_turno"

    


def ejecutar_accion_especial(jugador, accion_especial):
    """Ejecutar lógica para acciones especiales."""

    print("\n¡Acción especial activada!")
    numero_aleatorio = random.randint(1, 100)
    print(f"Numero: {numero_aleatorio}")
    print("Adivina un número entre 1 y 100 (1 intento):")

    votantes_extra = []

    try:
        adivinanza = int(input("> "))

        if adivinanza == numero_aleatorio:
            print("¡Increíble, lo adivinaste! ¡Ganaste votantes adicionales!")

            if accion_especial["impacto"]["especial"] == "trump_assasination_attempt":
                # Generar 1000 votantes demócratas
                # jugador.add_score(1000)
                # num_votantes=750 + 250 que se generan po defecto
                votantes_extra = generar_votantes(turno, jugador.name, num_votantes=750, impacto=accion_especial["impacto"])
            elif accion_especial["impacto"]["especial"] == "russian_hacking_attempt":
                # Generar 1000 votantes republicanos
                # jugador.add_score(1000)
                # num_votantes=750 + 250 que se generan po defecto
                votantes_extra = generar_votantes(turno, jugador.name, num_votantes=750, impacto=accion_especial["impacto"])
            
            print("¡Votantes adicionales generados con éxito!")
            return votantes_extra
                
        else:
            print(f"No es correcto. El número era {numero_aleatorio}. \nGracias por jugar, más suerte la próxima vez.")
            print("(Aunque fallaste, la controversia generó atención.)")
            votantes_radicales = generar_votantes(turno, jugador.name, num_votantes=44, impacto=accion_especial["impacto"])
            return votantes_radicales
    
    except ValueError:
        print(f"Entrada no válida. El número era {numero_aleatorio}. \nGracias por jugar, más suerte la próxima vez.")

    # Retornar lista vacía si falla
    return votantes_extra




def manejar_turno(turno, jugador):
    turno_jugador(jugador, turno)
    input(f"Turno del jugador {jugador.name.capitalize()} completado. Presiona ENTER para que juegue el rival...")




def turno_jugador(jugador, turno):
    """Lógica principal para un turno de un jugador."""

    print(f"\n\n\n**** TURNO {turno}: JUGADOR {jugador.name.upper()} ****")
    # print(f"Fecha: {fechas_turnos[turno - 1].strftime('%Y/%m/%d')}")
    # Formatear la fecha: "5 de Noviembre de 2024"
    fecha_formateada = formatear_fecha(fechas_turnos[turno - 1])
    
    print(f"Fecha: {fecha_formateada}")
    print(f"Presupuesto actual: ${formatear_numero(jugador.money)}")

    # Generar opciones una vez por turno
    acciones_turno = mostrar_opciones(jugador)

    # Bandera para controlar el flujo del turno
    flag_turno = True
    votantes_extra = []

    # Permitir repetir si el jugador elige análisis
    while flag_turno:
        # Mostrar opciones al jugador
        accion_seleccionada = elegir_accion(jugador, acciones_turno)

        # El jugador pasa el turno
        if accion_seleccionada is None:
            print(f"{jugador.name.capitalize()} ha pasado este turno. El impacto de esta medida será aleatorio")
            flag_turno = False
            votantes_aleatorios = generar_votantes(turno, jugador.name, num_votantes=random.randint(1,300))
            return votantes_aleatorios

        # Procesar la acción seleccionada
        if accion_seleccionada["nombre"] == "Análisis de datos":
            ejecutar_analisis(jugador, accion_seleccionada["coste"])

            # Mostrar presupuesto actualizado tras análisis
            print(f"\nPresupuesto actualizado tras análisis: ${formatear_numero(jugador.money)}")

            # Permitir elegir nuevamente
            continue
        
        # Acciones normales
        jugador.money -= accion_seleccionada["coste"]
        print(accion_seleccionada["descripcion"])

        if "especial" in accion_seleccionada["impacto"]:
            votantes_extra = ejecutar_accion_especial(jugador, accion_seleccionada)

        # Salir del bucle tras ejecutar una acción válida
        flag_turno = False


    print(f"\nPresupuesto restante: ${formatear_numero(jugador.money)}")

    
    # Generar votantes aplicando impacto o lista vacia para especial o pasar turno
    if accion_seleccionada:
        if "especial" not in accion_seleccionada["impacto"]:
            # Acción estándar: generar votantes con el impacto de la acción
            votantes = generar_votantes(turno, jugador.name, num_votantes=250, impacto=accion_seleccionada["impacto"])
        else:
            # Acción especial: no generar votantes regulares aquí
            votantes = []
    else:
        # Caso donde el jugador pasa turno
        votantes = []

    # Unir votantes normales y votantes adicionales (si existen)
    votantes_totales = votantes + votantes_extra
    print("¡Votantes generados con éxito!")

    # Procesar y mostrar votos
    procesar_votos(votantes_totales, democrata, republicano)
    
    return votantes




def procesar_votos(votantes, democrata, republicano):
    """Contar votos, asignar puntajes y mostrar resultados."""

    # Contar votos del turno
    votos = Counter([votante["voto"] for votante in votantes])
    print("\n==== PUNTUACIÓN ====")
    print(f"Resultados del turno: \n{votos}")

    # Asignar puntaje al jugador
    democrata.add_score(votos['democrata'])
    republicano.add_score(votos['republicano'])
    print(f"Puntuación actual: \n{republicano.name}: {republicano.score} - {democrata.name}: {democrata.score}")
    print("====================")
    return votos




print("**** Bienvenido a mis Primeras Elecciones EEUU ****")
print("\t(con clara del rey analytica)")
print()


# Crear jugadores: 1M$ inicial
democrata = Player("Democrata", 1000000)  
republicano = Player("Republicano", 1000000)


# Fechas turnos distribuidas equitativamente
fechas_turnos = calcular_fechas_turnos(fecha_inicial, fecha_final)


# Bucle de turnos
for turno in range(1, TURNOS_TOTALES + 1):

    if turno % 2 != 0:
        manejar_turno(turno, democrata)
    else:
        manejar_turno(turno, republicano)


print("\n\n\n**** PARTIDA FINALIZADA: RESULTADOS ELECTORALES ****")
print("Fecha: 5 de Noviembre de 2024")
print(f"{democrata.name}: {democrata.score}")
print(f"{republicano.name}: {republicano.score}")

if democrata.score > republicano.score:
    print(f"¡Ganador: {democrata.name}!¡Enhorabuena!")
elif democrata.score < republicano.score:
    print(f"¡Ganador: {republicano.name}!¡Enhorabuena!")
else:
    print("Pensábamos que era imposible, pero ha habido un... ¡empate!")

print("¡Gracias por jugar!")