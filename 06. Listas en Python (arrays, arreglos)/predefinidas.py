cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Iglesias"]
numeros = [1, 2, 5, 8, 3, 4]

#Ordenar 
print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
cantantes.append("Natos y waor")
cantantes.insert(1, "David Bisbal") #Con este método tienes que indicar el indice
print(cantantes)

#Eliminar elementos
cantantes.pop(1)
cantantes.remove("Drake") #Nombre exactamente igual que en la lista
print(cantantes)


#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print("Drake" in cantantes)#Con la palabra in, puedes buscar un elemento de la lista y te da un dato booleano (true)

#Contar elementos
print(cantantes)
print(len(cantantes))#len es para contar caracteres

#Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#Conseguir índice (la posición)
print(cantantes.index("Bad Bunny"))

#Unir listas
cantantes.extend(numeros) #Esto se le como -> a cantantes añadele la lista de numeros
print(cantantes)