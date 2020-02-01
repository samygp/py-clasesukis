#Parte 1
print("""
Los arreglos son colecciones de variables de un mismo tipo que
son nombradas bajo el mismo nombre de variable.
Entonces si quiero guardar 5 números, en vez de hacer algo como
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

Puedo asignar un arreglo con números, cada uno separado por comas:
mi_variable = [valor1, valor2, valor3, valor4]
Estos valores pueden venir de un número, cadena, booleano,
o cualquier otro valor, y puede ser explícitamente declarado,
o sea, escribir el valor, o asignarlo con una variable.
""")
num1 = 1
num3 = 3
print("Mis numeritos contendrán los números del 1 al 5:")
numeritos = [num1, 2, num3, 4, 5]
print(numeritos)

#Parte 2
print("""
Esto hace que todos mis numeritos estén contenidos en el nombre
"numeritos", y cada uno tiene un índice, entonces para hacer
referencia o usar cualquier elemento específico en un arreglo
debo usar su número de índice, que se escribe entre corchetes [].
El índice de los elementos empieza en 0, y el último índice
va a ser el tamaño de tu arreglo menos 1. O sea, si tu arreglo
tiene 5 elementos, el primer índice es "0", y el último índice
va a ser el "4".
""")
print("El primer elemento, en el índice 0 de mis numeritos es:", numeritos[0])
print("El último elemento, en el índice 4 de mis numeritos es:", numeritos[4])

#Parte 3
print("""
Para saber la longitud (tamaño) de un arreglo, se puede utilizar
len(), (abreviación de "length" - longitud), que recibe como parámetro 
un arreglo, o una variable que haga referencia a un arreglo.
""")
la_longitud = len(numeritos)
print("La longitud de mi arreglo de numeritos es:", la_longitud)

print("""
Ahora quiero que me muestre el último elemento (recordando que es 
la longitud, menos 1)
Porque si hago referencia a un índice que no existe, va a tronar 
como chilacayote".
""")

print("Entonces el último elemento es lo que guardé en 'la_longitud', menos 1: ", numeritos[la_longitud - 1])
#Si quieres que truene como chilacayote y te muestre un error, quita el comentario "#"

#De la siguiente línea:
#print(numeritos[1234])
#Va a decir que el índice fuera de rango y el error va a imprimir "IndexError: list index out of range"

#O esta línea:
#print(numeritos[la_longitud])