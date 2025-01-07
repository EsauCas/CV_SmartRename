# CV_SmartRename
Desarrollé un script en Python para automatizar el proceso de renombrar archivos en un directorio. Este proyecto permitió practicar la manipulación de archivos, el uso de estructuras de control y la interacción con el usuario.

Explicación Técnica del Código

    Objetivo General:
        El script busca en una carpeta específica y permite al usuario modificar los nombres de los archivos, reemplazando un texto dado con otro, de forma automatizada.

    Paso a Paso del Código:
        Importación de librerías: Se usó el módulo os para trabajar con directorios y gestionar las operaciones de archivos.
        Configuración inicial: El script especifica la carpeta donde se encuentran los archivos (carpeta) y los lista utilizando os.listdir, lo que permite trabajar con todos los archivos en esa ubicación.
        Interacción con el usuario: Solicita al usuario el texto a buscar en los nombres de los archivos y el texto por el que desea reemplazarlo, lo que demuestra habilidades en la programación interactiva.
        Bucle para renombrar archivos: Para cada archivo en la carpeta:
            Se construye la ruta de origen (origen) y la nueva ruta con el nombre modificado (destino).
            El archivo es renombrado usando os.rename, aplicando el reemplazo del texto especificado.
        Este enfoque asegura que los cambios sean dinámicos y adaptables a las necesidades del usuario.

    Habilidades Demostradas:
        Manipulación de rutas y nombres de archivos con os.
        Iteración con estructuras de control como bucles.
        Uso de cadenas de texto para personalizar procesos (búsqueda y reemplazo).
        Implementación de entrada dinámica mediante input, mejorando la flexibilidad del programa.

Impacto del Proyecto

Este script automatizó una tarea que normalmente se realiza manualmente, ahorrando tiempo y reduciendo errores. Fue útil para aprender principios básicos de automatización y trabajar con sistemas de archivos, habilidades clave en proyectos más avanzados relacionados con el manejo de datos o desarrollo de software.
