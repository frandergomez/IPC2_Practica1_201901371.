import os
import graphviz

# Diccionario de colores y sus códigos
colores = {
    'A': 'blue',
    'R': 'red',
    'V': 'green',
    'P': 'purple',
    'N': 'orange',
}

def crear_tablero(n, m):
    tablero = [[' ' for _ in range(m)] for _ in range(n)]
    return tablero

def mostrar_tablero(tablero):
    n = len(tablero)
    m = len(tablero[0])
    
    for i in range(n):
        for j in range(m):
            print(tablero[i][j] + '|', end=' ')
        print()

def colocar_pieza(tablero, fila, columna, color):
    tablero[fila][columna] = color[0]
    mostrar_tablero(tablero)

def generar_diagrama(tablero):
    dot = graphviz.Digraph(format='png')
    n = len(tablero)
    m = len(tablero[0])
    
    for i in range(n):
        for j in range(m):
            if tablero[i][j] != ' ':
                color = colores.get(tablero[i][j], 'black')
                dot.node(f'{i}_{j}', label='', shape='square', color=color, style='filled')
    
    for i in range(n):
        for j in range(m):
            if i < n - 1:
                dot.edge(f'{i}_{j}', f'{i+1}_{j}')
            if j < m - 1:
                dot.edge(f'{i}_{j}', f'{i}_{j+1}')
    
    dot.render('tablero', view=True)

def main():
    print("Bienvenido al programa de creación de tablero y colocación de piezas.")
    
    while True:
        print("\nMenu:")
        print("a. Crear tablero")
        print("b. Mostrar datos del estudiante")
        print("c. Salir")
        
        opcion = input("Seleccione una opción (a/b/c): ")
        
        if opcion == 'a':
            n = int(input("Ingrese el ancho del tablero: "))
            m = int(input("Ingrese el largo del tablero: "))
            tablero = crear_tablero(n, m)
            
            while True:
                mostrar_tablero(tablero)
                color = input("Seleccione un color (A/R/V/P/N) o 's' para salir: ").upper()
                
                if color == 'S':
                    break
                
                fila = int(input("Ingrese la fila donde desea colocar la pieza: "))
                columna = int(input("Ingrese la columna donde desea colocar la pieza: "))
                
                if 0 <= fila < n and 0 <= columna < m:
                    colocar_pieza(tablero, fila, columna, color)
                else:
                    print("Posición inválida. Inténtelo de nuevo.")
            
            generar_diagrama(tablero)
        
        elif opcion == 'b':
            print("Carnet del estudiante: 201901371")
            print("Nombre completo del estudiante: Frander Oveldo Carreto Gómez")
            print("Nombre del curso y sección: Introduccion a la programación 2 D")
        
        elif opcion == 'c':
            print("Saliendo del programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()