from random import *
colores = ['azul','rojo','blanco']
aleatorio = randint(1,50) #random en un rango
aleatorio2 = round(uniform(1,5),2) #random en un rango y decimal
aleatorio3 = random() #randon sin rango decimal
aleatorio4 = choice(colores) #1 randon de una lista
numeros = list(range(5,50,5)) #lista del 5 al 50 de 5 en 5 (no incluye el 50)


print(aleatorio)
print(aleatorio2)
print(aleatorio3)
print(aleatorio4)
print(numeros)
shuffle(numeros) #desordenar lista de manera random
print(numeros)





