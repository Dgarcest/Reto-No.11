#2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

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

def multiplicar_matrices():
    matriz_resultante = [] #se crea una variable que va a ser el resultado
    for i in range(len(matriz1)): # Recorre las filas de la primera matriz
        fila_resultante = [] 
        for j in range(len(matriz2[0])): # Recorre las columnas de la segunda matriz
            producto = 0
            for k in range(len(matriz1[0])): # Recorre las columnas de la primera matriz o las filas de la segunda matriz, ya que ambas tienen el mismo tamaño
                producto += matriz1[i][k] * matriz2[k][j]
            fila_resultante.append(producto) #se añade la variable producto (con las sumas) a "fila_resultante"
        matriz_resultante.append(fila_resultante) #se agrega a la matriz_resultante

    return matriz_resultante 

if __name__ == "__main__":
    #se piden las 2 matrices
    print("Recuerde que para multiplicar matrices, el numero de columnas de la primera matriz debe ser igual al numero de filas de la segunda matriz")
    matriz1_filas = int(input("escriba el número de filas que tiene la primera matriz: "))
    matriz1_columnas = int(input("escriba el número de columnas que tiene la primera matriz: "))
    matriz2_filas = int(input("escriba el número de filas que tiene la segunda matriz: "))
    matriz2_columnas = int(input("escriba el número de columnas que tiene la segunda matriz: "))
    
    #si no cumple la condicion no se multiplicaran las matrices
    if matriz1_columnas != matriz2_filas:
       print("La suma no se puede realizar porque el numero de columnas de la primera matriz debe ser igual al numero de filas de la segunda matriz")

    else:
        #se piden los valores de las matrices (con la funcion "crear_matriz")
        print("A continuacion escriba los valores de la primera matriz: ")
        matriz1 = crear_matriz(matriz1_filas, matriz1_columnas)
        print("A continuacion escriba los valores de la segunda matriz: ")
        matriz2 = crear_matriz(matriz2_filas, matriz2_columnas)

        #se imprimen las 2 matrices
        print("la primera matriz es: ")
        for i in range(len(matriz1)):
            print(matriz1[i])
        print("la segunda matriz es: ")
        for i in range(len(matriz2)):
            print(matriz2[i])
    
        #se multiplican las 2 matrices con la función "multiplicar_matrices"
        matriz_final = multiplicar_matrices()
        print("Y la multiplicación de las 2 matrices es: ") #se imprime la matriz resultante
        for i in range(len(matriz_final)):
            print(matriz_final[i])