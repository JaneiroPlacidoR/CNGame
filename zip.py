nombres = ['Ana','Lugo','Valeria']
edades = [20,30,45]
ciudades = ['Lima','Madrid']


combinados = list(zip(nombres,edades,ciudades))

print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} years y vive en {ciudad}")