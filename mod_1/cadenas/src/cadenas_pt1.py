print("""
Una cadena (string) es una secuencia de caracteres.
Así de simple. Internamente funcionan similarmente
a los arreglos; son colecciones de elementos de un
mismo tipo de dato (caracter).
Las cadenas en Python se representan poniendo texto
encerrado entre comillas " o entre apóstrofes '.
Y al igual que cualquier otro tipo de dato, se puede
guardar en variables.
Por ejemplo: mi_cadena = "Tengo texto"
""")

mi_cadena = "Tengo texto"
print("Si imprimo lo que tiene mi_cadena:", mi_cadena)

print("""
En Python, igual que en algunos otros lenguajes, se puede
acceder a un caracter específico de la cadena usando el
índice de ese caracter, igual que en los arreglos.
""")
print("Lo que contiene mi_cadena[0]:", mi_cadena[0])
print("Lo que contiene mi_cadena[1]:", mi_cadena[1])

print("""
Igual que en los arreglos, se pueden obtener secciones
o "slices" de una cadena utilizando rangos entre los corchetes
donde especificamos el índice.
""")


print("Los primeros 5 caracteres (mi_cadena[:5]):", mi_cadena[:5])
print("Los últimos 5 caracteres (mi_cadena[-5:])", mi_cadena[-5:])
print("Los caracteres del tercero al octavo(mi_cadena[2:8])", mi_cadena[2:8])
print("Todos los caracteres, en saltos de 2 (mi_cadena[::2])", mi_cadena[::2])

print("""
Los strings también pueden utilizar algunos operadores aritméticos:
El de suma y el de multiplicación.
Cuando se utiliza la suma (+ o +=) se concatenan dos strings
(se combinan las dos cadenas).
Por ejemplo, si hago print(mi_cadena + " aqui mero, obtenemos:
""")
print(mi_cadena + " aqui mero")
print("Pero eso no se guarda en la variable, sólo lo utiliza en ESA operación (print, en este caso)")
print("mi_cadena sigue conteniendo solamente:", mi_cadena)

print("""
Si a mi_cadena le asigno mi_cadena += " aqui mero", la concatenación
se guarda en la misma variable.
""")
mi_cadena += " aqui mero"
print("Ahora, después de guardar la concatenación tengo en mi_cadena:", mi_cadena)

print("""
La concatenación con el operador '+' no está limitada a añadir una sola cadena,
se pueden concatenar todas las cadenas consecutivas que se desee.
Puedo, por ejemplo, concatenar de la siguiente forma.
Declaro una nueva variable texto2:
texto2 = "y sigo "
Y el resultado lo puedo asignar a otra variable:
mas_texto = mi_cadena + " aqui mero " + texto2 + "agregando más"
""")
texto2 = "y sigo "
mas_texto = mi_cadena + " aqui mero " + texto2 + "agregando más"
print(mas_texto)

print("""
Otro operador aritmético que se puede utilizar con cadenas
es el de multiplicación (* o *=).
Aunque este es menos común, ya que lo único que hace
es repetir la cadena por el número de veces que se le
multiplique.
Por ejemplo, si hacemos: print(mi_cadena * 4)
""")
print(mi_cadena * 4)

print("Y ahora asignamos mi_cadena *= 2")

mi_cadena *= 2
print("mi_cadena ahora contiene:", mi_cadena)