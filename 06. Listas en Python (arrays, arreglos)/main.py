'''
Listas en Python: Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podemos usar un indice numérico.
'''

pelicula = "batman"
peliculas = ["Batman", "spiderman", "el señor de los aniños"] #La lista se aplica con los corchetes, y su contenido se leeria desde el indice 0, 1, 2... 
cantantes = list(("2pac", "drake", "pitbull"))
years = list(range(2020, 2051)) #lista de años desde el 2020 - 2050
variada = ["Jose Manuel", 20, 4.4, True, "Hola"]

'''
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
'''

# Indices 
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El Hobit"
print(peliculas)

print(peliculas[1])#Se contaria desde el cero, entonces sacaria spiderman
print(peliculas[-2])#Se contaria desde atrás, y sacaria spiderman
print(cantantes[0:3])#Quiere decir que sacarias desde el indice 0 hasta el 3
print(peliculas[1:])# Se sacaria todos los elementos a partir del indice X, en este caso 1 
print(years[4:8])

# Añadir elementos a Lista
cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes)

# Recorrer lista 
'''
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)#.append para añadir nuevas peliculas a la lista creada anteriormente.


print("\n*******LISTADO DE PELICULAS***********")
for i, pelicula in enumerate(peliculas, start=1): # i Representa el índice del elemento en la lista, pero con la peculiaridad de que comenzará en 1 (porque hemos especificado start=1 en enumerate).
    print(f"{i}. {pelicula}") #enumerate() es una función incorporada en Python que permite iterar sobre una secuencia y obtener tanto el índice como el valor del elemento en cada iteración.
    #Por tanto, en el ultimo print estamos imprimiento el CONTADOR. PELICULA en un string :D
''' 

# Listas multidimensionales (Listas dentro de otras listas)
print("\n**********LISTADO DE CONTACTOS***********")
contactos = [
    ["Antonio", "antonio@antonio.com"],
    ["Luis", "luis@luis.com"],
    ["Pedro","pedro@pedrito.com"]
]

for contacto in contactos: #Este for, da valor a contacto
    print("\n")
    for elemento in contacto: #Creamos otro for, para que contacto le de valor a elemento
        print(elemento) #Si la variable contacto es [antonio, antonio@antonio.com], la iteracion sera antonio y antonio@antonio.com


