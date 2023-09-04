def crear_tablero():
    print("Opción 1: Crear tablero seleccionada")
    # Agrega aquí tu lógica para crear el tablero

def mostrar_datos_estudiante():
    print("Opción 2: Mostrar datos del estudiante seleccionada")
    # Agrega aquí tu lógica para mostrar los datos del estudiante

while True:
    print("*********  Menú  **********")
    print("1. Crear tablero")
    print("2. Mostrar datos del estudiante")
    print("3. Salir")
    print("***************************")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        crear_tablero()
    elif opcion == "2":
        mostrar_datos_estudiante()
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")