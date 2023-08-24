"""Leer n cantidad de pares (hasta el usuario decida detenerse, que siga preguntando después de un 
par y así consecutivamente) de números ingresados por el usuario, evaluar y mostrar en pantalla 
cual cuadrante del plano cartesiano pertenece, considerar que también pueden darse los casos de:
a.	Ordenada positiva o negativa
b.	Abscisa positiva o negativa
c.	Punto origen

1.	Leer todos los pares de números
2.	Anunciar que ya se leyeron todos los pares de números
3.	Mostar cuantos pares fueron leídos
4.	Mostar los resultados de a que cuadrante pertenecen cada par
Nota: Usar controlador más while. Para no usar in range.
Nota: Utilizar dos vectores, puede ser vec X y vec Y.
 """

"""Planteamiento del problema

Existen 5 posibles combinaciones dentro de un plano cartesiano, dado que
los laterales o abscisas le pertenecen a X y los verticales u ordenadas a Y:

(+x,+y)
(-x,+y)
(-x,-y)
(+x,-y)
(0,0)"""

# Aunque el ejercicio limita de forma imaginaria las combinaciones
# El programa no serviria si no tomo en cuenta las otros 4 posibles combinaciones

"""(0,+y)
(0,-y)
(+x,0)
(-x,0)"""

#Declaracion de variables

res = ""

#Declaracion de controlador

contro = True

#Declaracion de vector

x = []
y = []

#Declaracion de iteradores

i = 0
j = 0

#Declaracion de contador

contP = 0 #contP significa Contador de Pares

#Importacion de modulo

import os

print("Plano cartesiano")

while contro == True:
    x.append(int(input("Favor ingresar el primer valor del par: ")))
    y.append(int(input("Favor ingresar el primer valor del par: ")))

    contP +=1

    res = input("\n Opcion Si: s \n Opcion No: n \n¿Desea agregar otro par: ")
    
    while res != "s" and res != "n":
        print("Respuesta invalida, intente de nuevo")
        res = input("\n Opcion Si: s \n Opcion No: n \n¿Desea realizar otra operacion?: ")

    if res == "s":
        print("\nDe vuelta a agregar")
    elif res == "n":
        contro = False
        print("Fin de la lectura")


if len(x) == len(y):
    print("\nEl total de pares leidos fue: {}".format(contP))
    while i < len(x):
        print("-----------------------------------------------------------------")
        print ("\nEl valor de la abscisa es: {}".format(x[i]))
        print("\nEl valor de la ordenada es: {}".format(y[i]))

        if x[i] > 0 and y[i] > 0:
            print("\nLos valores {} y {} pertenecen al primer cuadrante".format(x[i],y[i]))
        elif x[i] < 0 and y[i] > 0:
            print("\nLos valores {} y {} pertenecen al segundo cuadrante".format(x[i],y[i]))
        elif x[i] < 0 and y[i] < 0:
            print("\nLos valores {} y {} pertenecen al tercer cuadrante".format(x[i],y[i]))
        elif x[i] > 0 and y[i] < 0:
            print("\nLos valores {} y {} pertenecen al cuarto cuadrante".format(x[i],y[i]))
        elif x[i] == 0 and y[i] == 0:
            print("\nLos valores {} y {} pertenecen al punto de origen ".format(x[i],y[i]))
        elif x[i] == 0 and y[i] > 0:
            print("\nNo se encuentra el valor de abscisa dado que es {} y el valor {} pertenece a su ordenada positiva".format(x[i],y[i]))
        elif x[i] == 0 and y[i] < 0:
            print("\nNo se encuentra el valor de abscisa dado que es {} y el valor {} pertenece a su ordenada negativa".format(x[i],y[i]))
        elif x[i] > 0 and y[i] == 0:
            print("\nEl valor {} pertenece a su abscisa postiva y no se encuentra el valor de ordenada dado que es {} ".format(x[i],y[i]))
        elif x[i] < 0 and y[i] == 0:
            print("\nEl valor {} pertenece a su abscisa negativa y no se encuentra el valor de ordenada dado que es {} ".format(x[i],y[i]))
        else:
            print("Opcion no valida")
        os.system("pause")
        i += 1