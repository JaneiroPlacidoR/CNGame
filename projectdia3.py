#Crear analizador de texto en el cual el usuario
#ingrese un texto y 3 letras y el programa realizara 5 analisis

#1-Cuantas veces aparecen cada letra
#2-Cuantas palabras hay en total
#3-Primera y ultima letra
#4-Palabras en orden inverso
#5-Aparece Python?

texto = input('Introduzca un texto\n')
letras = [1,2,3]
letras[0] = input('Introduzca letra 1:\n')
letras[1] = input('Introduzca letra 2:\n')
letras[2] = input('Introduzca letra 3:\n')

#1#2#3S
parrafo = tuple(texto)

#2
spliteado = texto.split()

#4
alrevez = str(texto[::-1])
print(type(alrevez))

#5
isPython = "python" in texto
dic = {True:'si',False:'no'}


print(f'La letra {letras[0]} aparece {parrafo.count(letras[0])} veces\n'
      f'La letra {letras[1]} aparece {parrafo.count(letras[1])} veces\n'
      f'La letra {letras[2]} aparece {parrafo.count(letras[2])} veces\n'
#2
      f'El texto introducido tiene un total de {len(spliteado)} palabras\n'
#3
      f'La primera letra del texto es {parrafo[0]} y la ultima letra es {parrafo[len(parrafo)-1]}\n' #tambien se puede hacer con parrafo[-1]
#4
      f'El texto inverso es: {alrevez}\n'
#5
      f'Aparece la palabra python? {dic[isPython]}')


