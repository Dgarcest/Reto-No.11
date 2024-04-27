#3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

def crear_matriz(argumento_matriz_fila, argumento_matriz_columna):#funcion para pedir y guardar los valores de una matriz
    #se crean 2 listas, la matriz final y una para las filas de la matriz
    matriz = []
    fila_matriz = []
    for i in range(argumento_matriz_fila): #ciclo que se repitira el # de filas de la matriz (recorre filas)
        for j in range(argumento_matriz_columna): #ciclo que se repitira el # de columnas de la matriz (recorre cada elemento de la fila)
            valor = float(input(f"Escriba los valores de la matriz en orden ({i+1} fila y {j+1} columna): ")) #se pide cada valor (cada j son los valores de 1 fila completa)
            fila_matriz.append(valor) #cuando termina la 1era iteración vamos a tener los valores de la primera fila (aca se van agregando a la lista "fila_matriz")
        matriz.append(fila_matriz) #despues se agregan todos los valores de la fila a la lista "matriz" (en cada i se agrega una fila completa)(el proceso es fila por fila)
        fila_matriz=[] #se vacia la lista "fila_matriz" porque aún tiene los valores de la fila anterior, y al vaciarla se reinicia el proceso con los valores de la siguiente fila
    return matriz #al final la funcion retorna la lista "matriz" cuando terminan los 2 ciclos con todas las filas y columnas completas 

def matriz_transpuesta(matriz):
    matriz_final = []
    fila_matriz_transpuesta = []
    for i in range(len(matriz[0])): #recorre las columnas de la matriz
        for j in range(len(matriz)): #recorre las filas de la matriz
            fila_matriz_transpuesta.append(matriz[j][i]) #intercambia los indices de matriz original (para hacer la matriz transpuesta)
        matriz_final.append(fila_matriz_transpuesta) #pone la fila de la matriz transpuesta a la matriz final
        fila_matriz_transpuesta = [] #se vacia la fila para reiniciar el proceso
    return matriz_final


if __name__ == "__main__":
    #se pide el numero de filas y columnas de la matriz para hacer su transpuesta
    matriz_filas = int(input("escriba el número de filas que tiene la matriz: "))
    matriz_columnas = int(input("escriba el número de columnas que tiene la matriz: "))
    
    #se piden los valores de las matrices (con la funcion "crear_matriz")
    print("A continuacion escriba los valores de la matriz: ")
    matriz = crear_matriz(matriz_filas, matriz_columnas)

    #se imprime la matriz
    print("la matriz es: ")
    for i in range(len(matriz)):
        print(matriz[i])

    matriz_t = matriz_transpuesta(matriz) #se llama a la funcion
    #se imprime la matriz transpuesta
    print("la matriz transpuesta es: ")
    for i in range(len(matriz_t)):
        print(matriz_t[i])