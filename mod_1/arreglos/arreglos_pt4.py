print("""
Nota: esto es exclusivo de Python, las clases de índices
a continuación no son notación común en la mayoría de 
los lenguajes de programación, pero en Python son MUY
convenientes, y nos permiten hacer operaciones que en
otros lenguajes llevarían más trabajo de lograr.
""")

#Primera parte
print("""
Las listas en python tienen más de una forma de acceder
a los elementos, utilizando sus índices en más formas.
Se puede, por ejemplo, utilizar índices con valores negativos
para obtener elementos contando desde el final de la lista.
Esto significa que para obtener el último elemento de un arreglo,
en vez de averiguar la longitud del arreglo, restarle uno,
y utilizar ese número como índice, podemos mejor obtener
el elemento del índice "-1" en nuestra lista.
Con un arreglo: arr = [3, 5, 8, 1, 9, 12, 4]
Podemos obtener el último elemento haciendo lo siguiente.
""")
arr = [3, 5, 8, 1, 9, 12, 4]
print("arr[-1]:", arr[-1])
print("El penúltimo elemento sería arr[-2]:", arr[-2])
print("Y así sucesivamente")

#Segunda parte
print("""
En ocasiones necesitaremos sólo fragmentos del arreglo,
o "rebanadas" (slices). Estos sub-arreglos se pueden obtener
usando índices en forma de rangos (desde índice A hasta índice B).
El resultado de esto nos devuelve otra lista, con la selección
de los elementos contenidos en ese rango.
La notación en Python para obtener slices es de la siguiente
forma: arreglo[desde:hasta].
Cabe notar que el índice inferior (desde) es inclusivo
(incluye el elemento en ese índice), pero el índice
superior es exclusivo (excluye el elemento de ese índice).
Usando nuestro arreglo anterior, si quiero los elementos 
DESDE el primero (índice 0) HASTA el cuarto (índice 3), puedo
hacerlo de la siguiente forma.
""")
print(arr)
print("arr[0:4] devuelve:", arr[0:4])

print("""
Si deseamos obtener desde el primer elemento hasta algún otro
también podemos omitir el índice 0, y dejar vacío el primer
índice, y sólo especifiando el final del rango.
""")
print("arr[:4] es equivalente a arr[0:4] obtenemos:", arr[:4])

print("""
Análogamente, si omitimos el segundo parámetro, Python asume
que la selección implica ir hasta el final del arreglo.
""")
print("Todos los elementos desde el tercer índice: arr[3:] obtenemos:", arr[3:])
print("Si se omiten ambos, devuelve el slice del arreglo entero arr[:] obtenemos:", arr[:])

#Tercera parte
print("""
Esta forma de obtener slices también funciona con índices negativos.
""")
print(arr)
print("Puedo obtener los últimos 3 elementos usando índices negativos, arr[-3:] obtenemos:", arr[-3:])
print("Y puedo obtener los elementos desde el principio hasta antes de los últimos tres con arr[:-3] obtenemos:", arr[:-3])

#Cuarta parte
print("""
La última parte que se puede especificar en los índices de un slice
es con un tercer parámetro que indica los "saltos" entre un elemento
y el siguiente del slice.
Por ejemplo, si queremos un slice que nos devuelva los primeros 5 elementos,
pero en saltos de dos (omitir un elemento de cada dos) podemos hacer lo siguiente:
""")
print("El arreglo contiene:", arr)
print("Primeros cinco elementos, en saltos de 2, arr[0:5:2] obtenemos:", arr[0:5:2])
print("Ahora todos los elementos, en saltos de 3, arr[::3] obtenemos:", arr[::3])

print("""
Cuando utilizamos los saltos con índice negativo, el slice estará
en orden invertido.
""")

print("Todos los elementos, al revés, arr[::-1]", arr[::-1])

print("""
Atención: Cuando queremos obtener los últimos elementos con saltos
negativos, SE DEBE OMITIR EL ÍNDICE 0, de otra manera
Python lo interpreta de forma literal: 
Desde el índice 0 hasta el negativo especificado, y como el arreglo
no tiene en realidad índices negativos, el slice estará vacío.
""")
print("El arreglo contiene:", arr)
print("Los últimos 3 elementos, en orden invertido, arr[:-4:-1] obtenemos", arr[:-4:-1])
print("Slice mal especificado, arr[0:-4:-1] obtenemos:", arr[0:-4:-1])