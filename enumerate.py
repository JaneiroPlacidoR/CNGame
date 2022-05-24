lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

    #o
for indice,item in enumerate(lista):
    print(indice,item)

#con range
for indice,item in enumerate(range(50,58)):
    print(indice,item)


    #volver lista en un lista de taples
mis_taples = list(enumerate(lista))
print(mis_taples)


    #practica 1

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

    # practica 2

    lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre[0]=='M':
     print(f'{indice}')