#Imprimir e mayuscula
dic = {'c1':['a','b','c'],
       'c2':['d','e','f']}

print((dic['c2'][1]).upper())

#Agregar elementos a un diccionario creado
dic = {1:'a',2:'b'}
dic[3] = 'c'
print(dic)

#Sobreescribir
dic[2] = 'B'
print(dic)

#Ver todas las claves
print(dic.keys())
#Ver todos los valores
print(dic.values())
#Ver todos los elementos
print(dic.items())

miDic = {'nombre':'Karen',
         'apellido':'Jurgens',
         'edad':35,
         'ocupacion':'Periodista'}

#reasignando valores
miDic['edad'] = 36
miDic['ocupacion'] = 'Editora'

#creando nuevo campo en diccionario
miDic['Pais'] = "Colombia"

print(f'Este es mi diccionario: {miDic}')

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

#Sacando valores
mi_dict['puntos']['points2'][1] = 400
print(mi_dict['puntos']['points2'][1])


