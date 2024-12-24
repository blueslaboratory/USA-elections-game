# Date: 23/12/2024

import time
import select
import sys

import random
from acciones import accion_analisis, acciones_democratas, acciones_republicanas
from players import Player
from generador import generar_votantes
from collections import Counter

# Duracion del turno. Estándar: 5 minutos
MINUTOS = 1




def mostrar_opciones(jugador):
    """Mostrar las opciones disponibles para el jugador."""
    if jugador.name.strip().lower() == "democrata":
        return random.sample(acciones_democratas, 3) + [accion_analisis]
    else:
        return random.sample(acciones_republicanas, 3) + [accion_analisis]




def elegir_accion(jugador, acciones_turno):
    """Permitir al jugador elegir una acción."""

    # Mostrar opciones al jugador
    print("\nOpciones disponibles:")
    for i, accion in enumerate(acciones_turno):
        # Determinar el formato del coste
        if accion['coste'] < 0:
            # Formato para costes negativos
            coste_formateado = f"(Ingreso: +{abs(accion['coste'])}$)"
        else:
            # Formato para costes positivos
            coste_formateado = f"(Coste: {accion['coste']}$)"

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
                print(f"No tienes dinero suficiente para esta acción. Dinero actual: ${jugador.money}. \n¿Quieres pasar? (yes/no)")
                pasar = input("> ").strip().lower()
                if pasar == "yes":
                    print("Has pasado este turno.")
                    jugador_elija = False
                    return None
                else:
                    print("Selecciona otra opción.")
            else:
                jugador_elija = False
                return accion_seleccionada

        except ValueError:
            print("Entrada no válida. Por favor selecciona un número entre 1 y 4.")




def ejecutar_analisis(jugador, coste):
    """Ejecutar la lógica de análisis de datos."""

    jugador.money -= coste

    print("\n¡Has elegido: Análisis! (El análisis no consume turno)")
    print("\nProcesando los datos de los votantes...")
    print(f"Tienes {MINUTOS} minutos para procesar los datos con NiFi, realizar consultas en MongoDB \no consultar gráficos y estadísticas en Jupyter/Spark")
    input("\nPresiona ENTER para comenzar. Si acabas antes de tiempo vuelve a presionar ENTER...")

    try:
        for remaining in range(MINUTOS*60, 0, -1):
            # Pausa de 1 segundo
            time.sleep(1)

            # Mensajes al jugador
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

    try:
        adivinanza = int(input("> "))

        if adivinanza == numero_aleatorio:
            print("¡Increíble, lo adivinaste! ¡Ganaste votantes adicionales!")

            if accion_especial["impacto"]["especial"] == "trump_assasination_attempt":
                # Generar 1000 votantes demócratas
                jugador.add_score(1000)
                # votantes_extra = generar_votantes(turno, "Democrata", num_votantes=1000)
            elif accion_especial["impacto"]["especial"] == "russian_hacking_attempt":
                # Generar 1000 votantes republicanos
                jugador.add_score(1000)
                # votantes_extra = generar_votantes(turno, "Republicano", num_votantes=1000)
            
            print("¡Votantes adicionales generados con éxito!")
                
        else:
            print(f"No es correcto. El número era {numero_aleatorio}. \nGracias por jugar, más suerte la próxima vez.")
    
    except ValueError:
        print(f"Entrada no válida. El número era {numero_aleatorio}. \nGracias por jugar, más suerte la próxima vez.")




def manejar_turno(turno, jugador):
    turno_jugador(jugador, turno)
    input(f"Turno del jugador {jugador.name} completado. Presiona ENTER para que juegue el rival...")




def turno_jugador(jugador, turno):
    """Lógica principal para un turno de un jugador."""

    print(f"\n\n\n**** TURNO {turno}: JUGADOR {jugador.name.upper()} ****")
    print(f"Presupuesto actual: ${jugador.money}")

    # Generar opciones una vez por turno
    acciones_turno = mostrar_opciones(jugador)

    # Bandera para controlar el flujo del turno
    flag_turno = True

    # Permitir repetir si el jugador elige análisis
    while flag_turno:
        # Mostrar opciones al jugador
        accion_seleccionada = elegir_accion(jugador, acciones_turno)

        # El jugador pasa el turno
        if accion_seleccionada is None:
            print(f"{jugador.name.capitalize()} ha pasado este turno.")
            flag_turno = False
            continue

        # Procesar la acción seleccionada
        if accion_seleccionada["nombre"] == "Análisis de datos":
            ejecutar_analisis(jugador, accion_seleccionada["coste"])

            # Mostrar presupuesto actualizado tras análisis
            print(f"\nPresupuesto actualizado tras análisis: ${jugador.money}")

            # Permitir elegir nuevamente
            continue
        
        # Acciones normales
        jugador.money -= accion_seleccionada["coste"]
        print(accion_seleccionada["descripcion"])

        if "especial" in accion_seleccionada["impacto"]:
            ejecutar_accion_especial(jugador, accion_seleccionada)

        # Salir del bucle tras ejecutar una acción válida
        flag_turno = False


    print(f"\nPresupuesto restante: ${jugador.money}")

    # Generar votantes sin aplicar impacto
    votantes = generar_votantes(turno, jugador.name, num_votantes=250)
    # Generar votantes aplicando impacto
    # generar_votantes(turno, jugador.name, accion_seleccionada["impacto"])
    print("¡Votantes generados con éxito!")

    # Procesar y mostrar votos
    procesar_votos(votantes, democrata, republicano)
    
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
print("(con clara del rey analytica)\n")

# Crear jugadores: 1M$ inicial
democrata = Player("Democrata", 1000000)  
republicano = Player("Republicano", 1000000)


# Bucle de turnos
for turno in range(1, 9):

    if turno % 2 != 0:
        manejar_turno(turno, democrata)
    else:
        manejar_turno(turno, republicano)


print("\n\n\n**** PARTIDA FINALIZADA ****")
print(f"{democrata.name}: {democrata.score}")
print(f"{republicano.name}: {republicano.score}")

if democrata.score > republicano.score:
    print(f"¡Ganador: {democrata.name}!¡Enhorabuena!")
elif democrata.score < republicano.score:
    print(f"¡Ganador: {republicano.name}!¡Enhorabuena!")
else:
    print("Pensábamos que era imposible, pero ha habido un... ¡empate!")

print("¡Gracias por jugar!")