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

# Definición de la clase Nodo para la lista simplemente enlazada
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

# Definición de la clase ListaEnlazada para representar la matriz
class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self, fila):
        nuevo_nodo = Nodo(fila)
        if not self.inicio:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

# Clase Tablero que contiene la matriz del juego
class Tablero:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matriz = ListaEnlazada()
        for _ in range(n):
            fila = [' ' for _ in range(m)]
            self.matriz.insertar(fila)

    def mostrar_tablero(self):
        actual = self.matriz.inicio
        for i in range(self.n):
            print('|'.join(actual.dato) + '|')
            actual = actual.siguiente

    def colocar_pieza(self, fila, columna, color):
        actual = self.matriz.inicio
        for i in range(fila):
            actual = actual.siguiente
        actual.dato[columna] = color[0]

    def generar_diagrama(self):
        dot = graphviz.Digraph(format='png')
        actual = self.matriz.inicio
        for i in range(self.n):
            for j, color in enumerate(actual.dato):
                if color != ' ':
                    color_hex = colores.get(color, 'black')
                    dot.node(f'{i}_{j}', label='', shape='square', color=color_hex, style='filled')
            actual = actual.siguiente

        for i in range(self.n):
            for j in range(self.m):
                if i < self.n - 1:
                    dot.edge(f'{i}_{j}', f'{i+1}_{j}')
                if j < self.m - 1:
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
            tablero = Tablero(n, m)
            
            while True:
                tablero.mostrar_tablero()
                color = input("Seleccione un color (A/R/V/P/N) o 's' para salir: ").upper()
                
                if color == 'S':
                    break
                
                fila = int(input("Ingrese la fila donde desea colocar la pieza: "))
                columna = int(input("Ingrese la columna donde desea colocar la pieza: "))
                
                if 0 <= fila < n and 0 <= columna < m:
                    tablero.colocar_pieza(fila, columna, color)
                else:
                    print("Posición inválida. Inténtelo de nuevo.")
            
            tablero.generar_diagrama()
        
        elif opcion == 'b':
            print("Carnet del estudiante: 201901371")
            print("Nombre completo del estudiante: Frander Oveldo Carreto Gómez")
            print("Nombre del curso y sección: Introduccion a la programacion 2 D")
        
        elif opcion == 'c':
            print("Saliendo del programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()