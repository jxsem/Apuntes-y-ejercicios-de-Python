nombre = "Jose Manuel"


## Funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str) #Aqui decimos si la variable, es un entero (por ejemplo.. podemos usar los tipos de datos que queramos)
if comprobar: # Cuando haces esta comparacion no hace falta poner == True o false, ya el programa lo da por hecho
    print("Esa variable es un string")
else:
    print("No es una cadena/string")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales.")

# Limpiar espacios
frase = "              Mi contenido   "
print(frase) # Te muestra los espacios
print(frase.strip())# Quitar los espacios

#Eliminar variables
year = 2022
print(year)

del year
#print(year)

#Comprobar variable vacia

texto = " ff "

if len(texto) <= 0: #len -> lenght = longitud de una variable, entonces decismo, que si leng(de_la_variable) es menor o igual a cero...
    print("La variable está vacia")
else:
    print("La variable tiene contenido ", len(texto))

# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida")) #Te busca en que posición/caracter numero tal.

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Mayusuclas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())