cliente = {'nombre':'Federico', 'edad':75, 'ocupacion':'insructor'}
pelicula= {'titulo':'Matrix', 'ficha_tecnica':
    {'protagonista':'Keanu Reeves','director':'lana'}
           }
elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
     case {'nombre':nombre, 'edad':edad, 'ocupacion':ocupacion}:
         print("Es un cliente")
         print(nombre,edad,ocupacion)
     case {'titulo':titulo, 'ficha_tecnica':
    {'protagonista':protagonista,'director':director}}:
         print("Es una pelicula")
         print(titulo, protagonista, director)
     case _:
      print("No se que es esto")