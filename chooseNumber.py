from random import randint

print('Choose the number\nEste juego consiste en que debes adivinar el numero del 1-100.\nTienes 8 intentos y luego de'
      ' cada uno el juego te dira si el numero correcto es mayor o menor.\nAdemas te dira si estas '
      'Muy Frio, Frio, Caliente o Muy Caliente (osea) si te estas acercando o alejando del numero correcto')

nombre = input("Escribe tu nombre para continuar");


cont = 0
win = 0
numeroR = randint(1,101)

print(numeroR)

def calienteFrio(numero,numeroR):
    if numero == numeroR:
        print('Win!')
    elif (abs(numero - numeroR)) < 6:
        print('Muy Caliente')
    elif (abs(numero - numeroR)) < 11:
        print('Caliente')
    elif (abs(numero - numeroR)) < 50:
        print('Frio')
    else:
        print('Muy Frio')



while(cont<8 and win<1):
 numero = int(input("Escribe un numero:"))
 match numero:
   case numero if numero == numeroR:
       win = 1
   case numero if numero <= 0 | numero > 100:
    print('Numero no valido')
   case numero if numero < numeroR:
    cont += 1
    if cont < 8:
     print(f'Numero {numero} incorrecto, te quedan {8-cont} intentos, numero correcto es mayor')
     calienteFrio(numero,numeroR)
   case numero if numero > numeroR:
    cont += 1
    if cont < 8:
     print(f'Numero {numero} incorrecto, te quedan {8-cont} intentos, numero correcto es menor')
     calienteFrio(numero, numeroR)
   case _:
     print(f'Numero {numero} incorrecto, te quedan {8 - cont} intentos, numero correcto es menor')
else:
  if win == 1:print(f'Numero {numero} correcto, Ganaste! a los {cont+1} intentos')
  else:print(f'Numero {numero} incorrecto, te quedan {8-cont} intentos.\n El numero correcto era *{numeroR}*\n GAME OVER')





