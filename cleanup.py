# Date: 25/12/2024

import os
import shutil



def borrar_carpetas():
    carpetas_a_borrar = ["datos_votantes", "__pycache__"]

    for carpeta in carpetas_a_borrar:
        if os.path.exists(carpeta):
            try:
                shutil.rmtree(carpeta)
                print(f"Carpeta '{carpeta}' eliminada correctamente.")
            except Exception as e:
                print(f"Error al intentar eliminar la carpeta '{carpeta}': {e}")
        else:
            print(f"Carpeta '{carpeta}' no encontrada, no es necesario eliminarla.")



# si ejecutas cleanup.py directamente, se ejecuta el bloque bajo el nombre de main
if __name__ == "__main__":
    borrar_carpetas()
    print("Preparación completada. ¡Clean Up se ejecutó con éxito!")