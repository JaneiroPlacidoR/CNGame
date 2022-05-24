#contar valores repetidos dentro de tuple
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(int(mi_tupla.count(2)))

#convertir tuple en lista
mi_tuplaL = list(mi_tupla)
print(type(mi_tuplaL))

#extraer elementos
mi_tupla = (1, 2, 3, 4)

a,b,c,d = mi_tupla

print(a,c,d,b)