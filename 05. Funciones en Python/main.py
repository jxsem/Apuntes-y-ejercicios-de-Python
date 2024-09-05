#Funciones -> ¿Qué es una función?
'''
¿Qué es una función?
Piensa en una función como una receta en un libro de cocina. 
Una receta te dice exactamente cómo hacer algo, paso a paso. 
En programación, una función hace lo mismo: es un conjunto de instrucciones que realiza una tarea específica.
'''
#Para hacer la función se usa la palabra clave def
def saludar():
    print("Hola")

'''
Desglose de la función:
def: Esta palabra clave le dice a Python que estás definiendo una función.
saludar: Este es el nombre de la función. Puedes llamarlo como quieras, pero es mejor darle nombres que describan lo que hace la función.
(): Los paréntesis se usan para poner información adicional que la función podría necesitar. En este caso, no necesitamos ninguna información adicional, así que los dejamos vacíos.
:: Los dos puntos indican que el cuerpo de la función viene a continuación.
print("Hola"): Esta es la instrucción dentro de la función. Le dice a la computadora que imprima la palabra "Hola".
'''
#Para usar una función, simplemente la "llamamos" por su nombre
saludar()

#FUNCIONES CON PARAMETROS
'''
A veces, las funciones necesitan información adicional para hacer su trabajo. Esta información se llama parámetros y se ponen dentro de los paréntesis cuando definimos la función.

Por ejemplo, si queremos una función que salude a una persona por su nombre, podríamos hacerlo así:
'''
def saludar(nombre):
    print("Hola, " + nombre)

#Aquí, nombre es un parámetro. Cuando llamamos a la función, le damos un valor para nombre
saludar("María")

#FUNCIONES DEVOLVIENDO UN VALOR (RETURN)
'''
Algunas funciones realizan un cálculo y luego devuelven un valor. Para hacer esto, usamos la palabra clave return.

Por ejemplo, una función que suma dos números y devuelve el resultado:
'''
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)


'''
Variables locales: Son las que se definen dentro de la función
y no se pueden usar fuera de ella. A no ser que se haga un return

Variables globales: Se declaran fuera de la funcion y estan dentro y fuera de la función. (Las normales vaya)
'''

frase = "Si fuera kerio, pogba fuera sio top 5 mejores de su pais"

print(frase)
def holaMundo():
    frase = "Hola mundo"
    print("Dentro de la función: ")
    print(frase)

    year = 2021
    print(year)
    
    global website #global -> para que puedas usarla fuera de la función
    website = "victorroblesweb.es"
    print("Dentro: ", website)
    return "Dato devuelto " + str(year)
    

print(holaMundo())
print("FUERA: ", website)
