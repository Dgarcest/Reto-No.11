#4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

#se importa la funcion "crear_matriz" del archivo "Reto11punto1"
from Reto11punto1 import crear_matriz

def sumador_columnas(matriz, columna):
    suma = 0
    for i in range(len(matriz)): # Recorre filas
        suma += matriz[i][columna-1] #suma el valor de la fila y la columna dada (con -1 por el range que comienza en 0)
    return suma #la funcion retorna la suma de los valores de las 2 funcione

if __name__ == "__main__":
    #se pide el numero de filas y columnas de la matriz
    matriz_filas = int(input("escriba el número de filas que tiene la matriz: "))
    matriz_columnas = int(input("escriba el número de columnas que tiene la matriz: "))
    
    #se piden los valores de las matrices (con la funcion "crear_matriz")
    print("A continuacion escriba los valores de la matriz: ")
    matriz = crear_matriz(matriz_filas, matriz_columnas)

    print("la matriz es: ")
    for i in range(len(matriz)):
        print(matriz[i])

    #se pide que columna es la que se va a sumar
    columna_sumar = int(input("Escriba la columna que quiere sumar: "))
    suma_total = sumador_columnas(matriz, columna_sumar)
    print(f"la suma de la columna escogida es: {suma_total}")