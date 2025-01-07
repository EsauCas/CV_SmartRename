import os

carpeta = 'direccion/de/los/archivos'
lista_archivos = os.listdir(carpeta)
texto_buscar = input("Introduce el texto a buscar: ")
texto_reemplazar = input("Introduce el texto de reemplazo: ")

for nombre_archivo in lista_archivos:
    origen = os.path.join(carpeta, nombre_archivo)
    destino = os.path.join(carpeta, nombre_archivo.replace(texto_buscar, texto_reemplazar))
    os.rename(origen, destino)
