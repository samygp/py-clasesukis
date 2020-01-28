#Crea un arreglo vacío en una variable que se llame "el_arreglo"

###Crea tu arreglo aquí

###Ok, hasta aquí

print("El arreglo:", el_arreglo)

if len(el_arreglo) == 0:
    print("Bien, el arreglo está vacío")
else:
    print("El arreglo debe estar vacío, recuerda que se hace asignando el valor '[]' a tu variable")

#Apendiza el número 20, luego el 40, luego el 90

#Asigna los valores aquí

###Ok, hasta aquí

if el_arreglo == [20, 40, 90]:
    print("Bien, el arreglo tiene lo que debería tener")
else:
    print("Algo salió mal asignando los valores")


#Ahora agrega el número 100 al final del arreglo

#Asigna los valores aquí

###Ok, hasta aquí

if el_arreglo[len(el_arreglo) - 1] == 100:
    print("Bien, el arreglo tiene lo que debería tener")
else:
    print("Algo salió mal asignando los valores")


#Ahora agrega el valor 60 entre el 40 y el 90

###Asigna los valores aquí

###Ok, hasta aquí

if el_arreglo.index(60) == (el_arreglo.index(40) + 1):
    print("Bien, el arreglo tiene lo que debería tener")
else:
    print("Algo salió mal asignando los valores")


#Agrega el valor 80 entre el 60 y el 90

###Asigna los valores aquí

###Ok, hasta aquí

if el_arreglo.index(80) == (el_arreglo.index(90) - 1):
    print("Bien, el arreglo tiene lo que debería tener")
else:
    print("Algo salió mal asignando los valores")


#Remueve el valor que se encuentra en el índice 2, guárdalo en una variable
#que se llame "el_segundo"

###Completa el código aquí

###Ok, hasta aquí

if el_segundo == 60:
    print("Bien, ese era el valor correcto")
else:
    print("Algo no anda bien, el elemento en la variable 'el_segundo' debería ser igual a 60")


#Ahora remueve los dos últimos elementos del arreglo

###Completa el código aquí

###Ok, hasta aquí

print(el_arreglo)
if el_arreglo == [20, 40, 80]:
    print("Bien, el arreglo tiene lo que debería tener")
else:
    print("Algo salió mal asignando los valores")


#Ahora elimina los dos primeros elementos del arreglo

###Completa el código aquí

###Ok, hasta aquí

if el_arreglo == [80]:
    print("Bien, el arreglo tiene lo que debería tener")
else:
    print("Algo salió mal asignando los valores")