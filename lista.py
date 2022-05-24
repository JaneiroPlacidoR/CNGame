lista1 = ['a','n']
lista2 = [1,4]

lista2[1]='l' #cambiar eelemento de una lista
print(lista2)

#agregar
lista1.append('g')
print(lista1)
lista1.pop() #emilinar el ultimo elemento
eliminado = lista1.pop(0)

print(lista1,eliminado)
lista1.append('5')
print(lista1)
#ordenar
lista1.sort()
lista1.reverse()
print(lista1)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)


