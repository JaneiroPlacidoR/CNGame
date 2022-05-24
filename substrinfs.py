mi_texto = 'Esto es una prueba'
result = mi_texto.index('a', 11) #La a luego de la posicion 11
print(result, '---')
result = mi_texto[-4] #4to de atras para alante
print(result, '---')

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
result = frase.rindex("práctica") #buscar "practica" en reversa
print(result, '---')

result = frase[2:5]  # De posicion a posicion
print(result, '---')
result = frase[:5]  # Hasta la posicion
print(result, '---')
result = frase[2:5:2]  # de posicion a posicion saltando de
print(result, '---')
result = frase[::2]  # Todo saltando de
print(result, '---')
result = frase[::-1]  # Escribir al revez
print(result, '---')
