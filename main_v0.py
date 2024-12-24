# Date: 23/12/2024
# Simple Version: Sin encapsular, funcionando bien

import random
from acciones import accion_analisis, acciones_democratas, acciones_republicanas
from players import Player
from generador import generar_votantes
from collections import Counter



def turno_jugador(jugador, turno):

    # Turnos
    print(f"\n\n**** TURNO {turno}: JUGADOR {jugador.name.upper()} ****")
    print(f"Presupuesto actual: {jugador.money}$")


    # Seleccionar: 3 Acciones aleatorias + Análisis
    # random.sample: selecciona los elementos sin repeticion
    if jugador.name.strip().lower() == "democrat":
        acciones_turno = random.sample(acciones_democratas, 3) + [accion_analisis]
    else:
        acciones_turno = random.sample(acciones_republicanas, 3) + [accion_analisis]


    # Mostrar opciones al jugador
    print("\nOpciones disponibles:")
    for i, accion in enumerate(acciones_turno):
        print(f"{i + 1}. {accion['nombre']} - (Coste: ${accion['coste']})")


    # Capturar elección del jugador
    jugador_elija = True
    while jugador_elija:
        try:
            # Mostrar opciones y capturar entrada
            eleccion = int(input("\nSelecciona una opción (1-4): ")) - 1
            if eleccion not in range(len(acciones_turno)):
                raise ValueError
            
            accion_seleccionada = acciones_turno[eleccion]


            # Si elige análisis: NO PASA (You Shall Not Pass, porque no pasa) el turno
            if accion_seleccionada["nombre"] == "Análisis de datos":
                if accion_seleccionada["coste"] > jugador.money:
                    print("No tienes suficiente dinero para realizar el análisis.")
                    # Permitir que el jugador elija otra acción (por si esta la de funding)
                    continue 

                # Restar el costo del análisis
                jugador.money -= accion_seleccionada["coste"]
                print("\n¡Has elegido el análisis!")
                print("Procesando los datos de los votantes...")
                print("Tienes 5 minutos para procesar los datos con NiFi, realizar consultas en MongoDB \no consultar gráficos y estadísticas en Jupyter/Spark")
                input("Presiona ENTER si has acabado antes de tiempo...")
                print("Queda 1 minuto")

                # Lógica del análisis (puedes agregar más detalles)
                print("¡Se acabó el tiempo!¡Paren la investigación electoral!")
                print("Ahora puedes elegir una nueva acción en este turno. ¡Esta vez con más información! ¡Suerte!")
                # Volver al inicio del bucle sin penalizar el turno
                continue  


            # Aplicar impacto de la acción seleccionada
            if accion_seleccionada["coste"] > jugador.money:
                print("No tienes suficiente dinero para esta acción. ¿Quieres pasar? (yes/no)")
                pasar = input("> ").strip().lower()

                if pasar == "yes":
                    print("Has pasado este turno.")
                    jugador_elija = False
                else:
                    print("Selecciona otra opción.")

            else:
                jugador_elija = False

        except ValueError:
            print("Entrada no válida. Por favor selecciona un número entre 1 y 4.")
        

    jugador.money -= accion_seleccionada["coste"]
    print(accion_seleccionada["descripcion"])


    if "especial" in accion_seleccionada["impacto"]:
        print("\n¡Acción especial activada!")

        numero_aleatorio = random.randint(1, 100)
        
        print(f"Numero: {numero_aleatorio}")
        print("Adivina un número entre 1 y 100 (1 intento):")

        try:
            adivinanza = int(input("> "))
            if adivinanza == numero_aleatorio:
                print("¡Increíble, lo adivinaste! ¡Ganaste votantes adicionales!")
                
                if accion_seleccionada["impacto"]["especial"] == "trump_assasination_attempt":
                    # Generar 1000 votantes demócratas
                    jugador.add_score(1000)
                    # votantes_extra = generar_votantes(turno, "Democrata", num_votantes=1000)
                elif accion_seleccionada["impacto"]["especial"] == "russian_hacking_attempt":
                    # Generar 1000 votantes republicanos
                    jugador.add_score(1000)
                    # votantes_extra = generar_votantes(turno, "Republicano", num_votantes=1000)
                print("¡Votantes adicionales generados con éxito!")
                
            else:
                print(f"No es correcto. El número era {numero_aleatorio}. \n¡Mejor suerte la próxima vez!")

        except ValueError:
            print(f"Entrada no válida. El número era {numero_aleatorio}. \n¡Mejor suerte la próxima vez!")

    

    print(f"\nPresupuesto restante: {jugador.money}$")

    # Generar votantes sin aplicar impacto
    votantes = generar_votantes(turno, jugador.name, num_votantes=250)
    # Generar votantes aplicando impacto
    # generar_votantes(turno, jugador.name, accion_seleccionada["impacto"])
    print("¡Votantes generados con éxito!")



    # Contar votos del turno
    print("\n==== PUNTUACIÓN ====")
    votos = Counter([votante["voto"] for votante in votantes])
    print(f"Resultados del turno: {votos}")

    # Asignar puntaje al jugador
    democrata.add_score(votos['democrat'])
    republicano.add_score(votos['republican'])
    print(f"Puntuación actual: {democrata.name}: {democrata.score} - {republicano.name}: {republicano.score}")
    print("====================")


def manejar_turno(turno, jugador):
    turno_jugador(jugador, turno)
    input(f"Turno del jugador {jugador.name} completado. Presiona ENTER para que juegue el rival...")



# Crear jugadores: 1M$ inicial
democrata = Player("Democrat", 1000000)  
republicano = Player("Republican", 1000000)



# Bucle de turnos
for turno in range(1, 9):

    if turno % 2 != 0:
        manejar_turno(turno, democrata)
    else:
        manejar_turno(turno, republicano)



print("\n\n**** PARTIDA FINALIZADA ****")
print(f"{democrata.name}: {democrata.score}")
print(f"{republicano.name}: {republicano.score}")

if democrata.score > republicano.score:
    print(f"¡Ganador: {democrata.name}!¡Enhorabuena!")
elif democrata.score < republicano.score:
    print(f"¡Ganador: {republicano.name}!¡Enhorabuena!")
else:
    print("Pensábamos que era imposible, pero ha habido un... ¡empate!")

print("¡Gracias por jugar!")