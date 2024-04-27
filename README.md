# Reto-No.11

## 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

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

def sumar_matrices(): #funcion para sumar matrices
    #la matriz resultante va a ser por el momento igual a la matriz 1 (para que tenga las mismas filas y columnas)
    matriz_resultante = matriz1 #puede ser igual a la matriz 2 o igual a una matriz con solo ceros ya que despues estos valores van a cambiar
    #estos 2 ciclos recorren la matriz 1
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            #al obtener la ubicación de un valor se toma la misma ubicacion pero de la matriz 2 y se suman y se pone en la misma ubicacion pero en la matriz resultante, asi con todos los valores
            matriz_resultante[i][j] = matriz1[i][j] + matriz2[i][j] 
    return matriz_resultante #la funcion retorna la suma de los valores de las 2 funciones

if __name__ == "__main__":
    #se pide el numero de filas y columnas de las 2 matrices que se van a sumar
    matriz1_filas = int(input("escriba el número de filas que tiene la primera matriz: "))
    matriz1_columnas = int(input("escriba el número de columnas que tiene la primera matriz: "))
    matriz2_filas = int(input("escriba el número de filas que tiene la segunda matriz: "))
    matriz2_columnas = int(input("escriba el número de columnas que tiene la segunda matriz: "))
    
    #si las matrices tienen distintos tamaños no se podrán sumar
    if matriz1_filas != matriz2_filas or matriz1_columnas != matriz2_columnas:
       print("La suma no se puede realizar porque las matrices deben tener el mismo tamaño (mismas filas y columnas)")

    else:
        #se piden los valores de las matrices (con la funcion "crear_matriz")
        print("A continuacion escriba los valores de la primera matriz: ")
        matriz1 = crear_matriz(matriz1_filas, matriz1_columnas)
        print("A continuacion escriba los valores de la segunda matriz: ")
        matriz2 = crear_matriz(matriz2_filas, matriz2_columnas)

        #teniendo los valores de las 2 matrices se imprime cada una
        print("la primera matriz es: ")
        for i in range(len(matriz1)):
            print(matriz1[i])
        print("la segunda matriz es: ")
        for i in range(len(matriz2)):
            print(matriz2[i])
    
        #se suman las 2 matrices con la función "matriz_suma"
        matriz_suma = sumar_matrices()
        print("Y la suma de las 2 matrices es: ") #se imprime la matriz resultante
        for i in range(len(matriz_suma)):
            print(matriz_suma[i])
```
## 2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

## 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

## 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
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
```

## 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
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
```
