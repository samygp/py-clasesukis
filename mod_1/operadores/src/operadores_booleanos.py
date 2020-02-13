print("\n\n\n")

print("""
Los operadores Booleanos son los que nos permiten realizar
álgebra Booleana (operaciones lógicas).
Estas operaciones se realizan para evaluar condiciones, que
nos permiten controlar el flujo del programa, para que, basado
en una condición, algo suceda o no.
Los valores que representan el resultado de cualquier
operación Booleana en Python: "True" y "False"
""")
print("Imprimir un True:", True)
print("Imprimir un False:", False)

print("""
Estos valores se obtienen como resultado cuando se evalúa
una operación lógica. Las más básicas de estas operaciones son
comparar si dos valores son iguales "==", o diferentes "!=".
""")
print("1 es igual a 1?", 1 == 1)
print("1 es diferente de 1?", 1 != 1)
print("1 es igual a 2?", 1 == 2)
print("1 es diferente de 2?", 1 != 2)

print("""
Otras operaciones comunes con números es comparar si uno es
mayor que ">" o menor que "<" el otro.
""")
print("1 es menor que 1?", 1 < 1)
print("1 es mayor que 1?", 1 > 1)
print("1 es menor que 2?", 1 < 2)
print("1 es mayor que 2?", 1 > 2)
print("2 es mayor que 1?", 2 > 1)
print("2 es menor que 1?", 2 < 1)

print("""
Y estas operaciones tienen sus variaciones de menor o igual a "<="
y mayor o igual a ">="
""")
print("1 es menor o igual que 1?", 1 <= 1)
print("1 es mayor o igual que 1?", 1 >= 1)
print("1 es menor o igual que 2?", 1 <= 2)
print("1 es mayor o igual que 2?", 1 >= 2)
print("2 es mayor o igual que 1?", 2 >= 1)
print("2 es menor o igual que 1?", 2 <= 1)

print("""
Estos resultados se pueden igualmente guardar en variables.
Guardemos el resultado de si 1 es menor que 4.
""")
es_menor = 1 < 4
print("La variable 'es_menor' contiene:", es_menor)

print("""
Volviendo a por qué son útiles estas operaciones:
La forma en que controlamos el flujo de un programa es con enunciados de tipo "if",
que se traducen del inglés "if this, then that" (si esto, entonces aquello).
Esto significa que "Si mi condición se cumple, entonces haz esto".
El bloque que sigue al if debe estar indentado (indentación es el nombre que 
le dan a la sangría de texto en programación).
Por ejemplo:
""")
print("2 es menor que 3?")
if 2 < 3:
    print("Sí, 2 es menor que 3")

print("""
E igual que en un lenguaje natural/humano, podemos decir en el programa qué pasa
si nuestra condición no se cumple, utilizando la palabra "else"
(del inglés "o si no...")
""")
print("5 es mayor que 8?")
if 5 > 8:
    print("Sí, 5 es mayor que 8")
else:
    print("No, 5 no es mayor que 8")


print("""
Las variables que guardan un valor Booleano pueden usarse en las
condiciones de los enunciados "if"
""")
es_diferente = 5 != 9
print("5 es diferente de 9?")
if es_diferente:
    print("Sí, 5 es diferente de 9")
else:
    print("No, 5 no es diferente de 9")

print("""
Adicionalmente, podemos usar enunciados "elif" (abreviación de "else if")
Para decir que si no se cumplió la condición anterior, pero sí se cumple
una condición diferente, ocurra algo.
""")
es_igual = 9 == 8
es_menor = 9 < 8
print("9 es igual a 8?")
if es_igual:
    print("Sí, 9 es igual de 8")
elif es_menor:
    print("No, 9 es menor que 8")
elif 9 > 8:
    print("No, 9 es mayor que 8")
else:
    print("Ninguna de las anteriores")
    
