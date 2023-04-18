import os
import shutil

# Definir el nombre de la carpeta donde se moverán los archivos
# nueva_carpeta = "/ruta/a/la/nueva/carpeta"
nueva_carpeta = "/Users/Macbook/Desktop/capturas importantes"

# Obtener la ruta del escritorio
escritorio = os.path.join(os.path.expanduser("~"), "Desktop")

# Iterar a través de todos los archivos en el escritorio
for archivo in os.listdir(escritorio):
    # Si el nombre del archivo comienza con "Captura de Pantalla"
    if archivo.startswith("Captura de Pantalla"):
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(escritorio, archivo)
        # Mover el archivo a la nueva carpeta
        shutil.move(ruta_archivo, nueva_carpeta)
