# Bucle for ¿Qué es un bucle?
'''
Un bucle es una herramienta que nos permite repetir una serie de instrucciones varias veces sin tener que escribir el mismo código una y otra vez.
Es como si le dijeras a una persona: "Sigue haciendo esta tarea hasta que te diga que pares."

'''
for i in range(1, 6): #i es como una letra predeterminada que se usa como un contador.
    print(i)


# Esto le dice al ordenador: "Para cada número i desde 1 hasta 5, imprime el número i."
'''
Desglose del bucle for:
for i in range(1, 6): Significa "Para cada valor i en el rango de 1 a 5 (el 6 no está incluido)".
print(i): Esto le dice a la computadora que imprima el valor actual de i.
'''



# Bucle while

'''
Ahora imagina que quieres hacer algo pero no sabes cuántas veces necesitarás repetirlo, 
solo quieres que continúe hasta que cierta condición se cumpla. Por ejemplo, contar hasta que llegues a 5. 
Aquí es donde entra el bucle while.
'''
i = 1
while i <= 5:
    print(i)
    i += 1

'''
Desglose del bucle while:
i = 1: Empezamos con i igual a 1.
while i <= 5: Significa "Mientras i sea menor o igual a 5, sigue repitiendo lo que está dentro del bucle."
print(i): Esto le dice a la computadora que imprima el valor actual de i.
i += 1: Esto significa "Aumenta i en 1 cada vez que pases por aquí." Sin esta línea, i siempre sería 1 y el bucle nunca terminaría (esto se llama un bucle infinito).
'''

#Diferencias clave:
'''
Bucle for: Se usa cuando sabes cuántas veces quieres repetir algo.
Bucle while: Se usa cuando no sabes exactamente cuántas veces necesitas repetir algo, pero tienes una condición que te dice cuándo parar.
'''