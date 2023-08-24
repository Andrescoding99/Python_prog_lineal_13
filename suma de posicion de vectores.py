"""02.	Crear dos vectores y una cantidad de números determinada por el usuario, luego muestre la 
suma de los datos en ambos vectores para la misma posición:

a.	Si el resultado de la suma es positivo almacenar ese valor en un vector para valores positivos, 
de otro modo deberá ser almacenado en el vector para datos negativos
b.	Al finalizar deberá mostrar el resultado de cada caso, y preguntar al usuario que valores desea 
visualizar, positivos o negativos.

1.	Primero se lee todo-
2.	Al final se lee la información.
"""

#Declarando variables

valor = 0
suma = 0
res = ""
res1= ""

# Declarando el vector

v = [] #Primer vector normal
x = [] #Este es el vector para positivos
y = [] #Este es el vector para negativos
z = [] #Segundo vector normal

#Declarando el iterador

i = 0
j = 0
k = 0

#Importando modulo 

import os

#Declarando controlador

contro = True

# Lectura de datos / llenado del vector (lista)

print ("\nBienvenido")

i = int(input("Ingrese la cantidad de numeros que quiere meter para el primer y segundo vector: "))
while i <= 0:
    print("\nHa ingresado un valor fuera del rango para la cantidad de numeros, intente otra vez")
    i = int(input("Ingrese la cantidad de numeros que quiere meter: "))
print("\nValor de numeros aceptado\n") 

print("\nIngreso de numeros primer vector")

for j in range(i):
    v.append(float(input("\nFavor ingresar el numero {}: ".format(j+1)))) 

print("\nIngreso de numeros segundo vector")

for k in range(i):
    z.append(float(input("\nFavor ingresar el numero {}: ".format(k+1)))) 

print("\nNumeros ingresados")


print("\nPrimer vector\n")

i = 0 #Reinicializar el iterador

while i < len(v):
    print(v[i])
    i += 1

i = 0 #Reinicializar el iterador

print("\nSegundo vector\n")

while i < len(z):
    print(z[i])
    i += 1

#SUMA DE POSICIONES

j = 0 #Reinicializar el iterador

while j < len(v):
    suma = v[j] + z[j]
    if suma >= 0:
        x.append(suma)
    else:
        y.append(suma)

    j += 1

os.system("pause")

while contro == True:
    res = input("\nOpciones: \nMostrar valores positivos: p \nMostrar valores negativos: n \n¿Que valores desea ver: ")

    while res != "p" and res != "n":
        print("Ha ingresado una opcion invalida, intente de nuevo")
        res = input("¿Que valores desea ver: ")
    print("\nRespuesta aceptada")

    i = 0 #Reinicializar el iterador

    if res == "p":
        print("\nNumeros positivos")
        while i < len(x):
            print(x[i])
            i += 1
    else:
        print("\nNumeros negativos")
        while i < len(y):
            print(y[i])
            i += 1

    res1 = input("\n Opcion Si: s \n Opcion No: n \n¿Desea volver a mostrar los valores?: ")
    
    while res1 != "s" and res1 != "n":
        print("Respuesta invalida, intente de nuevo")
        res1 = input("\n Opcion Si: s \n Opcion No: n \n¿Desea volver a mostrar los valores?: ")

    if res1 == "s":
        print("\nDe vuelta a la muestra")
    elif res1 == "n":
        contro = False
        print("Fin de la lectura")


