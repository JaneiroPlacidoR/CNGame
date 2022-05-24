nombre = input('Cual es tu nombre?\n')
ventas = float(input('De cuanto fueron tus ventas\n'))
comisiones = round(ventas*0.13,2)
print(f'\t{nombre} \n \tTus comisiones de '
      f'este mes fueron de: {comisiones}')


