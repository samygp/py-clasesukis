print("""
Habrá ocasiones en que quieras sumar el resultado de una operación
en la misma variable, para no tener que crear un montón de variables
y tampoco usar tanta memoria (recuerda que cada variable abarca espacios de memoria)
Por ejemplo, tengo una variable contador, y le quiero sumar 1
""")
#Dato cool: cuando en una cadena escribes "\n", va a imprimir un salto de línea (como cuando presionas enter en Word)
print("\nContador parte 1:")
contador = 0
print(contador)

#A contador le sumo 1
contador = contador + 1
#Ahora contador vale 1
print(contador)

#A contador le sumo 1
contador = contador + 1
#Ahora contador vale 2
print(contador)


print("""
Aquí vas a aprender de un nuevo operador: "+="
Se utiliza += cuando tienes una variable a la que le quieres
agregar una cantidad. Hace lo mismo que la forma anterior, pero
con mucho menos texto
""")
print("\nContador parte 2:")
#Por ejemplo:
contador = 0
print(contador)

#A contador le sumo 1
contador += 1
#Ahora contador vale 1
print(contador)

#A contador le sumo 1
contador += 1
#Ahora contador vale 2
print(contador)


print("""
Y esto maravillosamente aplica para todas las
operaciones básicas aritméticas
""")
print("\nContador al reves:")
contador_al_reves = 3
print(contador_al_reves)
contador_al_reves -= 1
print(contador_al_reves)
contador_al_reves -= 1
print(contador_al_reves)
contador_al_reves -= 1
print(contador_al_reves)

print("\nDuplicador:")
duplicador = 2
print(duplicador)
duplicador *= 2 #Lo multiplico por 2 y lo guardo en la misma variable, ahora vale 2
print(duplicador)
duplicador *= 2 #Lo vuelvo a duplicar y lo guardo, ahora vale 4
print(duplicador)
duplicador *= 2 #Ahora vale 8
print(duplicador)

print("\nDividir cosito:")
#Otro dato cool, escribir el operador de multiplicación (*) dos veces significa
#Elevar a la "x" potencia. Por ejemplo 3 ** 5 significa "elevar 3 a la 5 potencia"
dividir_cosito = 3 ** 3
print(dividir_cosito)
dividir_cosito /= 3 #Lo divido entre 3 y lo guardo
print(dividir_cosito)
dividir_cosito /= 3 #Lo vuelvo a dividir entre 3
print(dividir_cosito)
dividir_cosito /= 3 #Lo vuelvo a dividir entre 3
print(dividir_cosito)