#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Acceder a los elementos de una lista: indexar
una_lista = ["Texto", 17, True, 17, 17]
print(una_lista[0])

# %% Acceder a los elementos de una tupla: indexar
una_tupla = ("Texto", 17, True, 17, 17)
print(una_tupla[0])

# %% Acceder a los elementos de una tupla: unraveling

valor_1, valor2 = ("Uno", 2)

# %% Cómo crear un diccionario
# Un diccionario está ordenado, no permite duplicados, y se puede cambiar
diccionario = {"nombre": "Juan",
               "edad": 32,
               "altura": 180,
               "casado": True}

print(diccionario)

#%% También se puede crear con la función dict()

diccionario = dict(nombre="Juan", edad=32, altura=180, casado=True)
print(diccionario)


#%%
'''La función zip en Python combina elementos de dos o más iterables 
(como listas, tuplas, etc.) en tuplas agrupadas. 
Cada tupla contiene elementos correspondientes de los iterables de entrada. 
Se detiene cuando el iterable más corto se queda sin elementos.'''
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c', 'd']

resultado = zip(lista1, lista2)
print(list(resultado))  # [(1, 'a'), (2, 'b'), (3, 'c')]

#%% Podemos usar zip para crear un diccionario rápidamente
d = dict(zip('abc', [1, 2, 3]))
print(d)

# %% Acceder a los elementos del diccionario
nombre = diccionario["nombre"]
print(nombre)

diccionario["nombre"] = "Pedro"
print(nombre)  # la variable no cambia al cambiar el diccionario

nombre = diccionario.get("nombre")
print(nombre)

# La clave tiene que existir, sino dará un error
error = diccionario["x"]
print(nombre)

# Podemos usar get para que devuelva un valor por defecto si la clave no existe
x = diccionario.get("x", "valor por defecto")
print(x)

# %% Añadir nuevo elemento al diccionario
print(diccionario)
diccionario["pareja"] = "Rosa"
print(diccionario)

'''El método update en los diccionarios de Python permite agregar o actualizar 
pares clave-valor desde otro diccionario o iterable de pares clave-valor 
al diccionario actual. Si una clave ya existe, su valor es sobrescrito; 
si no, el par clave-valor es agregado.'''

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}

#%% Ejemplo de update en el diccionario "diccionario"
diccionario.update({'estudios':'grado', 'casado': False})
print(diccionario)

# %% borrar elementos de un diccionario

diccionario.pop("nombre") # Borra el elemento asociado a la clave indicada
del diccionario["edad"]
diccionario.clear()  # borra todo el diccionario


#%% Ejercicio 1: Actualización y acceso a valores en un diccionario
''' Crea un diccionario con información de un estudiante y luego actualízalo.
Sigue los pasos:
1 - Define un diccionario inicial con los siguientes datos:
    nombre: Juan
    edad: 20
    grado: GCED
2 - El estudiante ha cambiado de carrera y ahora estudia "Matemáticas". 
    Actualiza el valor correspondiente.
3 - Añade una nueva clave 'promedio' con el valor 8.5.
4 - Imprime el diccionario actualizado.
5 - Accede e imprime solo el valor asociado con la clave 'edad'.

Salida esperada:
{
    'nombre': 'Juan',
    'edad': 20,
    'grado': 'Matemáticas',
    'promedio': 8.5
}
20

'''


#%% Solución al ejercicio 1:

# Diccionario inicial
estudiante = {
    'nombre': 'Juan',
    'edad': 20,
    'grado': 'GCED'
}

# Actualización del valor de la clave 'carrera'
estudiante['grado'] = 'Matemáticas'

# Agregar nueva clave 'promedio'
estudiante['promedio'] = 8.5

# Imprimir diccionario actualizado
print(estudiante)

# Acceder e imprimir el valor asociado a 'edad'
print(estudiante['edad'])

#%% Bucles: iterar sobre las claves
for clave in diccionario:
    print(clave)

# %% Bucles: iterar sobre las claves v2
for clave in diccionario.keys():
    print(clave)

# %% Bucles: iterar sobre las claves y acceder al valor
for clave in diccionario:
    print(diccionario[clave])

# %% Bucles: iterar sobre los values
for valor in diccionario.values():
    print(valor)

# %% Bucles: iterar sobre los items v1
for item in diccionario.items():
    print(item)
    
# %% Bucles: iterar sobre los items v2
for c, v in diccionario.items():
    print(c, " --> ", v)



#%% Ejercicio 2: Contar palabras con un diccionario
'''Escribe una función que cuente la frecuencia de palabras en una lista 
usando un diccionario, y que devuelva dicho diccionario.

1 - Usa como ejemplo la lista de palabras:
    palabras = ['manzana', 'pera', 'manzana', 'uva', 'pera', 'manzana']

2 - Crea la función que recibe la lista y devuelve el dict con las veces
    que aparece cada palabla.
    
3 - En el main, imprime el diccionario con las palabras como claves y 
    sus frecuencias como valores.

Ejemplo de salida esperada:
{
    'manzana': 3,
    'pera': 2,
    'uva': 1
}
'''

#%% Solución al Ejercicio 2

def contar_frecuencias(lista_palabras):
    frecuencia = {}
    
    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

# Ejecutar el programa principal
if __name__ == "__main__":
    # Lista de palabras
    palabras = ['manzana', 'pera', 'manzana', 'uva', 'pera', 'manzana']
    
    # Llamar a la función y obtener el diccionario de frecuencias
    resultado = contar_frecuencias(palabras)
    
    # Imprimir el resultado
    print("Frecuencia de palabras:", resultado)

# %% Copiar un diccionario (mal)

original = {
    "nombre": "Luisa",
    "edad": 27,
    "casado": False
}

copia = original

copia["nombre"] = "Ana"

print(original)
print(copia)

# %% Copiar un diccionario (bien)
original = {
    "nombre": "Luisa",
    "edad": 27,
    "casado": False
}

copia = original.copy()
copia["nombre"] = "Ana"
print(original)
print(copia)

#%% Ejercicio: Copia de Diccionarios
'''
Crea un programa que manipule copias de diccionarios sin alterar 
el original. 
Sigue los pasos:

1 - Define un diccionario que contenga información de un libro:

    libro = {
        'título': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'año': 1967,
        'precio': 20.0
    }
2 - Haz una copia superficial del diccionario usando el método 
adecuado y guárdala en otra variable.
3 - En la copia:
    Cambia el 'precio' a 15.0.
    Agrega una nueva clave 'género' con el valor 'Realismo mágico'.
    Imprime el diccionario original y la copia para comprobar que el original 
    no ha sido modificado.
'''

#%% Solución
def main():
    # Diccionario original
    libro = {
        'título': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'año': 1967,
        'precio': 20.0
    }

    # Crear una copia superficial del diccionario
    copia_libro = libro.copy()

    # Modificar la copia
    copia_libro['precio'] = 15.0
    copia_libro['género'] = 'Realismo mágico'

    # Imprimir el diccionario original
    print("Diccionario original:", libro)

    # Imprimir la copia modificada
    print("Copia modificada:", copia_libro)

if __name__ == "__main__":
    main()


#%% Ejercicio: Lista de Diccionarios
''' 
1 - Define una lista llamada estudiantes que almacenará información de varios 
    estudiantes, donde cada estudiante será un diccionario con las siguientes claves:
        'nombre'
        'edad'
        'carrera'
2 - Llena la lista con al menos tres diccionarios de estudiantes con información ficticia.

3 - Escribe un programa que:
    Recorra la lista de estudiantes e imprima el nombre y la carrera de cada uno.
    Agregue un nuevo estudiante a la lista pidiendo los datos al usuario.
    Permita modificar la carrera de un estudiante ya existente buscando por su nombre.
    Imprima la lista actualizada.
'''

#%% Solución Ejercicio: Lista de Diccionarios
def main():
    # Lista inicial con diccionarios de estudiantes
    estudiantes = [
        {'nombre': 'Juan', 'edad': 20, 'carrera': 'Ingeniería'},
        {'nombre': 'María', 'edad': 22, 'carrera': 'Arquitectura'},
        {'nombre': 'Carlos', 'edad': 19, 'carrera': 'Derecho'}
    ]

    # Imprimir información de cada estudiante
    print("Lista inicial de estudiantes:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Carrera: {estudiante['carrera']}")

    # Agregar un nuevo estudiante pidiendo datos al usuario
    print("\nAgrega un nuevo estudiante:")
    nuevo_nombre = input("Nombre: ")
    nueva_edad = int(input("Edad: "))
    nueva_carrera = input("Carrera: ")

    nuevo_estudiante = {'nombre': nuevo_nombre, 'edad': nueva_edad, 'carrera': nueva_carrera}
    estudiantes.append(nuevo_estudiante)

    # Modificar la carrera de un estudiante existente
    print("\nModifica la carrera de un estudiante:")
    nombre_a_modificar = input("Nombre del estudiante a modificar: ")

    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre_a_modificar:
            nueva_carrera = input("Nueva carrera: ")
            estudiante['carrera'] = nueva_carrera
            print(f"La carrera de {nombre_a_modificar} ha sido actualizada.")
            break
    else:
        print(f"No se encontró a ningún estudiante con el nombre {nombre_a_modificar}.")

    # Imprimir lista actualizada
    print("\nLista actualizada de estudiantes:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Carrera: {estudiante['carrera']}")

if __name__ == "__main__":
    main()
