print("\n\n\n")
#Parte 1
print("""
Se puede crear un arreglo vacío (es muy común)
asignando a una variable vacía el valor "[]"
""")
numeritos = []
print("Un arreglo vacío:", numeritos)

#Parte 2
print("""
Para añadir elementos al final de un arreglo (apendizar), puedes
utilizar la función "append(valor)" en la variable que representa el arreglo.
Este método requiere como parámetro el valor que se vaya a insertar dentro del
arreglo.
""")
print("Numeritos ahora contiene: ", numeritos, "y su longitud es:", len(numeritos))
print("Apendizando el número 20")
numeritos.append(20)
print("Ahora mis numeritos son:", numeritos, "y su longitud es:", len(numeritos))

print("Apendizando el número 30")
numeritos.append(30)
print("Ahora mis numeritos son:", numeritos, "y su longitud es:", len(numeritos))

print("Apendizando el número 50")
numeritos.append(50)
print("Ahora mis numeritos son:", numeritos, "y su longitud es:", len(numeritos))

print("Apendizando el número 50")
numeritos.append(60)
print("Ahora mis numeritos son:", numeritos, "y su longitud es:", len(numeritos))

#Parte 3
print("""
Para insertar un elemento en cualquier posición dentro del arreglo
(incluyendo el principio), se puede utilizar el método "insert(indice,valor)".
El método 'insert' requiere dos parámetros, el primero es el índice en el que
se quiere insertar un valor, y el segundo parámetro es el valor que se quiere
agregar en la lista.
Esta operación aumenta en 1 los índices de todos los elementos subsecuentes,
esto quiere decir que si se inserta en el índice 2, todos los demás
índices incrementarían en 1, o sea, el que antes era el índice 2, ahora será el 3,
el que solía ser el 3, ahora será el 4, y así sucesivamente.
""")
print("Mis numeritos ahora contienen: ", numeritos)
print("Por ejemplo, para insertar al principio (índice 0) el número 10, se utiliza 'arreglo.insert(0, 10)'")
numeritos.insert(0, 10)
print("Y después de insertarlo mis numeritos tienen: ", numeritos)
print("""
Ahora, para insertar el número 40 entre el 30 y el 50, que tienen actualmente
los índices 2 y 3 respectivamente, debemos insertar el 40 en el índice 3,
de tal forma que el 50, que actualmente está en la cuarta posición (índice 3),
será movido en una posición (será el índice 4, la quinta posición del arreglo).
""")
numeritos.insert(3, 40)
print("Y después de insertarlo mis numeritos tienen: ", numeritos)

#Parte 4
print("""
Y lo que el programador da, el programador quita.
Así como se pueden insertar y apendizar elementos en los arreglos, se
pueden remover y 'botar' objetos de un arreglo.
Para eliminar un elemento del final del arreglo, se puede utilizar la
operación 'pop()' (botar, como cuando bota el corcho de una botella), y
se utiliza sin parámetros (más adelante la usaremos diferente). 
Esta operación, además, devuelve (da como resultado) el objeto que
se acaba de botar.
""")
print("Ahora vamos a eliminar el último elemento haciendo pop, y guardarlo en una variable 'el_ultimo'")
el_ultimo = numeritos.pop()
print("El ultimo elemento fue:", el_ultimo, "y ahora mis numeritos contienen:", numeritos)

print("Eliminando el siguiente numero del final:", numeritos.pop(), "ahora mis numeritos contienen", numeritos)

#Parte 5
print("""
Por último, para eliminar un elemento en cualquier otro índice del arreglo
se puede utilizar el método 'arreglo.pop(indice)', que requiere como
parámetro el índice en el arreglo que se quiere eliminar.
Nota que utilizar 'pop' en índices que no son el último elemento
también ocasiona que los índices de cada elemento se reorganicen,
(todos los elementos subsecuentes al eliminado se reducirán en 1)
""")
print("Removiendo el primer elemento con numeritos.pop(0)")
uno_especifico = numeritos.pop(0)

print("Obtenemos que el primer elemento era:", uno_especifico, "y ahora mis numeritos contienen", numeritos)
print("Mi arreglo ahora contiene ", len(numeritos), "elementos, y eliminaré el que se encuentra en el índice 1")
print("El valor es:", numeritos.pop(1), "y al final mis numeritos contienen:", numeritos)