# Date: 23/12/2024

from config import output_folder
from generador import generar_votantes
from players import Player

from collections import Counter



# Crear jugadores: 1M$ inicial
democrata = Player("Democrat", 1000000)  
republicano = Player("Republican", 1000000)



# Bucle de turnos
for turno in range(1, 9):


    if turno % 2 != 0:
        jugador = democrata
    else:
        jugador = republicano

    print(f"\n**** TURNO {turno}: JUGADOR {jugador.name.upper()} ****")


    # Acción de turno (expandir/codificar)
    # accion(jugador)

    # Generar votantes
    votantes = generar_votantes(turno, jugador.name)
    print("¡Votantes generados con éxito!")

    # Contar votos del turno
    votos = Counter([votante["voto"] for votante in votantes])
    print(f"Resultados del turno: {votos}")

    # Asignar puntaje al jugador
    democrata.add_score(votos['democrat'])
    republicano.add_score(votos['republican'])
    print(f"Puntuacion actual:")
    print(f"{democrata.name}: {democrata.score} - {republicano.name}: {republicano.score}")

    # Presionar ENTER para continuar
    input(f"Turno del jugador {jugador.name} completado. Presiona ENTER para que juegue el rival...")


print("\n*** PARTIDA FINALIZADA ***")
print(f"Resultados finales: {democrata.name}: {democrata.score} vs {republicano.name}: {republicano.score}")