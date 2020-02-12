print("\n\n\n\n\n")
print("""
Los arreglos pertenecen a una categoría que llamamos "iterables".
Un iterable, se puede (duh...) iterar, o sea, puedes navegar/desplazarte/recorrerlo
elemento por elemento, paso a paso (iteración por iteración).
En el caso de los arreglos y listas, se pueden iterar usando su índice entre corchetes, 
pero si tuviera que siempre hacer referencia a los valores de un arreglo uno por uno,
tardaría muchísimo si quisiera imprimir algo como una lista de 200 números,
y tendría que escribir muchísimo texto. Entooonces, hay otra forma
mucho más pragmática y programática de iterar las cosas.
""")

print("""
En muchos lenguajes existe el ciclo "for". En la mayoría se interpreta
"for an element, as long as a condition is met, do this" (para un elemento,
mientras que se cumpla una condición, haz lo siguiente).
Por ejemplo, "para un número entero, mientras que el número sea menor a 10, súmale 1".
""")

print("""
Y pues, es bonito, y está bien, pero al dude que hizo Python (Guido Van Rossum)
Se le hacía no muy entendible (es suizo el vato), poco idiomático y muy
largo de explicar. Entonces en Python, la palabra "for" se interpreta como
"for each element in an iterable, do this" (por cada elemento en un iterable, haz esto).
Mucho más fácil de interpretar.

Ahora, si tengo mis numeritos en un arreglo, puedo imprimirlos de uno en uno así:
""")
numeritos = [1, 2, 3, 4, 5]
print(numeritos[0])
print(numeritos[1])
print(numeritos[2])
print(numeritos[3])
print(numeritos[4])

print("""
Pero no es nada práctico cuando el arreglo se vuelve más largo.
Y para quitarme mucha carga de escribir, mejor itero usando un
ciclo "for", para hacer algo "por cada elemento...".
Voy a hacer que por cada elemento me imprima ese elemento:
""")
for numero in numeritos:
    print(numero)

print("""
El nombre que le des a cada elemento del arreglo puede ser el que
tú quieras, pero lo importante está en recordar que ese nombre
o variable que representa a cada elemento, sólo tiene sentido DENTRO
del bloque indentado que representa al "for".
Cuando termina tu "for" y Python ejecuta la siguiente línea, el
nombre que le diste a tu variable va a representar el último valor
que tuvo en el for que acaba de terminar.
Por ejemplo, aquí voy a imprimir el valor de "numero",
estando fuera del bloque indentado del "for" anterior.
""")
print("Mi variable 'numero' contiene: ", numero)


print("""
Imprimir todo con un for es mucho más fácil de escribir, y de leer.
Pero no hay por qué detenerse ahí, se puede hacer lo que tú quieras
con cada elemento de un arreglo. Y puedes escribir tantas líneas como
necesites. Mientras sigan estando indentadas en el mismo bloque, pueden
seguir utilizando la variable temporal "numero".
Ahora voy a hacer que mi ciclo "for" me diga cuánto es el doble,
y también cuánto es la mitad de cada número:
""")
for numero in numeritos:
    print("Mi variable 'numero' ahora vale:", numero)
    print("El doble es:", numero*2)
    print("La mitad es: ", numero/2)


print("""
Como otro ejemplo, es mucho más fácil sumar todos los elementos de un arreglo
usando "for", para que por cada elemento, sume su valor a otra variable,
y al final imprima el resultado que calculé sumando todo:
""")
la_sumatoria = 0
for numero in numeritos:
    print("Hasta este punto, la sumatoria vale: ", la_sumatoria)
    print("Ahora le voy a sumar el numero: ", numero)
    la_sumatoria += numero

print("Y al final la sumatoria vale: ", la_sumatoria)

print("""
Ahora haremos otra operación que es común, vamos a encontrar el menor valor
de un arreglo desordenado. Para esto, primero tenemos que guardar en una variable el
primer valor del arreglo. Después, debemos recorrer el arreglo y comparar
cada número contra el que tenemos guardado en la variable. Si el número
que estamos iterando es menor que el que está guardado en la variable,
vamos a cambiar el valor guardado en la variable por el valor actual.
""")
arr = [90, 20, 50, 8, 123, 6, 8888, 15]
el_menor = arr[0]

#Iteramos cada elemento del arreglo
for numero in arr:
    print("\nEl número actual es:", numero)
    print("El menor número hasta ahora es:", el_menor)
    print(numero, "es menor que", el_menor, "?")
    if numero < el_menor:
        print("Sí,", numero, "es menor que", el_menor)
        el_menor = numero
    else:
        print("No,", numero, "no es menor que", el_menor)

print("\nEl menor número en el arreglo es:", el_menor)

print("\n¿Queda claro señooooores?\n\n")