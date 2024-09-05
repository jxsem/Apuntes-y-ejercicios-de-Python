#Condicional IF 

#La estructura del if es así: SI esto es IGUAL a esto -> imprime esto. Si NO, imprime lo otro.

color = input("Adivina cual es el color de la interfaz de Python que uso: ")

if color == "gris":
    print(f"Enhorabuena, el color era el {color}")
else:
    print("El color no es el correcto")

'''
# Operadores de comparación
== Igual
!= Diferente
< Menor que
> Mayor que
<= Menor o igual
>= Mayor o igual
'''

year = int(input("¿En que año estamos?: "))

if year >= 2021:
    print("Estamos desde 2021 en adelante")
else:
    print("Es un año anterior a 2021")

# IF ANIDADOS -> IF DENTRO DE IF

nombre = "Jose"
ciudad = "Granada"
continente = "Europa"
edad = 55
mayor_edad = 18

if edad >= mayor_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "Europa":
        print("El continente es diferente a Europa")
    else:
        print("Y es del continente de Europa")
else:
    print("No es mayor de edad")



#Elif para evaluar múltiples condiciones.
dia = 2

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")
