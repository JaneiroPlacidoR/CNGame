texto = input('ingrese un texto').lower()
letras = []
letra1 = 0
letra2 = 0
letra3 = 0

#1
for i in range(3):
 letras.append(input(f'ingrese letra {i+1}').lower())


print(f"La letra '{letras[0]}' aparece {texto.count(letras[0])} veces \n"
      f"La letra '{letras[1]}' aparece {texto.count(letras[1])} veces \n"
      f"La letra '{letras[2]}' aparece {texto.count(letras[2])} veces \n")
#2
palabras = texto.split()
print(len(palabras))
#3

print(f" Primela palabra: {palabras[0]} y Ultima palabra: {palabras[-1]}")

#4
textoReves = str(palabras[::-1])
print(textoReves)

#5
if 'python' in palabras:
 print("Python esta en palabras")
else:
 print("Python no esta en palabras")
