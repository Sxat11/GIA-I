#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%% ¿Qué es una variable booleana?
# Una variable booleana es un tipo de dato que solo puede tener dos valores:
#     - True  (verdadero)
#     - False (falso)
# Se utilizan comúnmente en condicionales para controlar el flujo del programa.

#%% Condicionales con variables booleanas

condicion_1 = True
condicion_2 = False

if condicion_1:
    print("condicion_1 es verdadera")

    
if condicion_2:
    print("condicion_2 es verdadera")  # No se ejecutará

#%% if simple

a = 3
b = 4

if a < b:
    print("a es menor que b")   

#%% if con else

a = 33
b = 33

if b > a:
    print("b es mayor que a")
else:
    print("b no es mayor a")

#%% condicionales encadenados (elif)

a = 200
b = 33

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")

#%% Otro ejemplo con if y else

a = 200
b = 33

if b > a:
    print("b es mayor que a")
else:
    print("b NO es mayor que a")

#%% Condiciones lógicas (and y or)

a = 200
b = 33
c = 100

# Se usan operadores lógicos para combinar condiciones
if a > b and c > a:
    print("Ambas condiciones son verdaderas")

#%% Condicionales anidados

x = 41

if x > 10:
    print("Mayor que 10,")
    if x > 20:
        print("y también que 20!")
    else:
        print("pero menor que 20.")

# Equivalente sin condicionales anidados, usando operadores booleanos
# Esta versión es más plana y puede facilitar la lectura si hay muchas ramas o niveles.
# Es útil cuando las condiciones se pueden expresar claramente sin necesidad de anidar.
if x > 20:
    print("Mayor que 10,")
    print("y también que 20!")
elif x > 10:
    print("Mayor que 10,")
    print("pero menor que 20.")

#%% Asignación condicional (operador ternario)

# En Python, puedes asignar un valor a una variable según una condición usando la sintaxis:
#   variable = valor_si_verdadero if condicion else valor_si_falso

edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# Esto es equivalente a:
# if edad >= 18:
#     mensaje = "Mayor de edad"
# else:
#     mensaje = "Menor de edad"

#%% Operadores booleanos disponibles en Python

# Operadores de comparación:
#   ==    igualdad
#   !=    distinto
#   >     mayor que
#   <     menor que
#   >=    mayor o igual que
#   <=    menor o igual que

# Operadores lógicos:
#   and   devuelve True si ambas condiciones son verdaderas
#   or    devuelve True si al menos una condición es verdadera
#   not   invierte el valor lógico (True → False, False → True)
