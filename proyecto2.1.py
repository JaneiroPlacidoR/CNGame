nombre = input('Cual es tu nombre')
ventas = int(input('De cuanto fueron tus ventas'))
comision = ventas * 0.13
print(f"{nombre} vendio {ventas} con una comision de {comision} para un sueldo total de {comision+ventas}")