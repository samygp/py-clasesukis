num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

#Crea un arreglo que contenga como primer elemento el primer número ingresado,
#como segundo número debe contener el segundo número ingresado,
#y como tercer número debe contener la suma de ambos.
#Intenta hacerlo sin declarar variables adicionales para guardar el resultado de la suma
#(calcúlalo dentro de la declaración del arreglo).
#Llama a la variable del arreglo "el_arreglo"

###Crea tu arreglo aquí

###Ok, hasta aquí

if el_arreglo[2] == (el_arreglo[0] + el_arreglo[1]):
    print("Bien, el arreglo tiene lo que debería tener")
else:
    print("Algo no anda bien, el último valor no equivale a la suma de los primeros dos")

#Imprime el valor de la longitud del arreglo
print("La longitud del arreglo es:")

#Imprime el arreglo entero
print("El arreglo completo es:")

#Asigna en una variable llamada "ultimo_indice" el valor del último índice.
#Calcúlalo apoyándote de la longitud del arreglo.
#Atención: para este punto la longitud del arreglo es "3",
#pero el último índice es 2.

###Calcula tu valor aquí


###Ok, hasta aquí

if el_arreglo[ultimo_indice] == (el_arreglo[0] + el_arreglo[1]):
    print("Bien, ese era el valor correcto")
else:
    print("Algo no anda bien, el último valor no equivale a la suma de los primeros dos")


#Crea un arreglo que tenga 6 elementos, llama a esta variable "otro_arreglo"

###Crea tu arreglo aquí

###Ok, hasta aquí

print(otro_arreglo)

#Imprime el elemento que está a la mitad del arreglo (debería ser el tercer elemento)
#Calcula el índice apoyándote de la longitud, y asígnalo a una variable que se llame "la_mitad".

###Calcula tu valor aquí


###Ok, hasta aquí

if otro_arreglo[int(la_mitad)] == otro_arreglo[2]:
    print("Bien, ese era el valor correcto")
else:
    print("Algo no anda bien, el último valor no equivale a la suma de los primeros dos")