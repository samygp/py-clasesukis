arreglo1 = [10, 20, 30, 40, 50]
num1 = 150
#Réstale a la variable num1 todos los valores contenidos en arreglo1
#usando un ciclo for

###Completa el código aquí

###Ok, hasta aquí

if num1 == 0:
    print("Bien, el resultado es correcto")
else:
    print("Algo salió mal calculando el resultado")


arreglo_doble = []
#Ahora, con un ciclo for, haz que la variable "arreglo_doble"
#tenga los números de 'arreglo1', pero multiplicados por 2 (el doble de cada número).
#Los números en 'arreglo_doble' deberán estar en el orden inverso que en
#'arreglo1'
#pista: lo puedes lograr recorriendo en orden el primer arreglo,
#e insertando el resultado de cada elemento como primer elemento de 'arreglo_doble'

###Completa el código aquí

###Ok, hasta aquí

if arreglo_doble == [100, 80, 60, 40, 20]:
    print("Bien, el resultado es correcto")
else:
    print("Algo salió mal calculando el resultado")


arreglo2 = [90, 20, 30, 89, 100, 1, -99, 91, 300, 5, 10, 56]
el_mayor = arreglo2[0]
#Encuentra el mayor número de arreglo2, guárdarlo en la variable 'el_mayor'
#No hace falta que imprimas cada iteración, sólo importa el resultado que
#guardes en 'el_mayor'

###Completa el código aquí

###Ok, hasta aquí

if el_mayor == 300:
    print("Bien, el resultado es correcto")
else:
    print("Algo salió mal calculando el resultado")

los_pares = []
los_impares = []
#Ahora, recorre arreglo1, arreglo2 y arreglo_doble (necesitarás tres ciclos for, uno por cada arreglo)
#En el arreglo 'los_pares' guarda todos los elementos de arreglo1 y arreglo2 que sean pares
#En el arreglo 'los_impares' guarda todos los elementos de arreglo1 y arreglo2 que sean impares

###Completa el código aquí

###Ok, hasta aquí

print("los impares:",len(los_impares), los_impares, "Los pares:", len(los_pares), los_pares)
if len(los_impares) == 5:
    print("El número de impares encontrados es correcto")
else:
    print("El número de impares encontrados es incorrecto")

if len(los_pares) == 17:
    print("El número de pares encontrados es correcto")
else:
    print("El número de pares encontrados es incorrecto")