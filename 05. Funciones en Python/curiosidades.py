def mi_funcion(nombre):
    return "Hola que tal" + nombre

def mi_segunda_funcion(apellidos):
    return "Hola que tal 2 " + apellidos #Las variables que esten definidas antes de invocarlas

nombre = "Jose"
apellidos = "Soldado"

print("Hola mundo")
print(f"Bienvenido, {nombre}")

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellidos))