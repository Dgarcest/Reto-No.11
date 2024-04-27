#5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

#se importa la funcion "crear_matriz" del archivo "Reto11punto1"
from Reto11punto1 import crear_matriz

def sumador_filas(matriz, fila):
    suma = 0
    for i in range(len(matriz[fila-1])): # Recorre los elementos de la fila escogida (con -1 por el range)
        suma += matriz[fila-1][i] #suma todos los elementos de una misma fila uno por uno
    return suma #la funcion retorna la suma de los valores de las 2 funciones

if __name__ == "__main__":
    #se pide el numero de filas y columnas de la matriz
    matriz_filas = int(input("escriba el número de filas que tiene la matriz: "))
    matriz_columnas = int(input("escriba el número de columnas que tiene la matriz: "))
    
    #se piden los valores de las matrices (con la funcion "crear_matriz")
    print("A continuacion escriba los valores de la matriz: ")
    matriz = crear_matriz(matriz_filas, matriz_columnas)

    #se imprime la matriz
    print("la matriz es: ")
    for i in range(len(matriz)):
        print(matriz[i])

    #se pide la fila que se va a sumar
    fila_sumar = int(input("Escriba la fila que quiere sumar: "))

    #se llama a la funcion y se imprime la suma de la filfa
    suma_total = sumador_filas(matriz, fila_sumar)
    print(f"la suma de la fila escogida es: {suma_total}")