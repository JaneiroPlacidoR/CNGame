names = ['Juan', 'Pablo', 'Pedro']
for item in names:
    if item[0] == 'P':  # si el elemento comienza con P/
        print(f'{names.index(item) + 1} {item}')
    elif item.startswith('J'):
        print(f'{names.index(item) + 1} {item}')

for letra in 'python':
    print(letra)

# con listas
for estatura, edad in [[170, 25], [160, 30]]:
    print(estatura)
    print(edad)

# con diccionarios
dic = {'Clave1': 'a', 'Clave2': 'b', 'Clave3': 'c'}
for item in dic.items():
    print(item)

# sumadora
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0
for item in lista_numeros:
    suma_numeros += item
print(suma_numeros)

#sumadora pares impares
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0
for item in lista_numeros:
    if item%2 == 0:
        suma_pares += item
    else:
        suma_impares += item
print(f'Suma de numeros pares: {suma_pares}\nSuma de numeros impares: {suma_impares}')


#tabla de multiplicar
cont = 1
num = int(input("introduce un numero:"))
while cont < 13:
    print(f'{num}x{cont}={num*cont}')
    cont+=1

numero = 50

while numero >= 0:
    if numero%5 == 0:
     print(numero)
    numero -= 1

#break
nombre = 'federico'
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#continue
nombre = 'federico'
for letra in nombre:
    if letra == 'r':
        continue  #omite eso que no se cumple y sigue
    print(letra)
#range
for numero in range(5):
    print(numero)

#rango del 1 incluyendo al 30

for numero in range(1,31):
    print(numero)

#range saltando

for numero in range(1,31,2):
    print(numero)

#asignando range a lista

lista = list(range(1,101))
print(lista)

x = 4
#potencia y raiz cuadrada
print(2**2,x**0.5)
