#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Un f-string permite insertar variables (o expresiones) dentro de texto
# se indica que es un f-string, y no un string normal, poniendo una f (o F) antes del texto 
# dentro del f-string se indican los huecos (placeholders) 
# donde insertaremos la expresión usando llaves {} y la expresión dentro de las llaves
# fuera de las llaves puede ir cualquier texto válido

# por ejemplo, imprimimos una variable donde guardamos un entero (int)
entero = 42
print(f'El valor es {entero}')
# en el placeholder se puede usar cualquier expresión válida de python
print(f'El valor^2 es {entero**2}')

# se puede indicar el formato con el que queremos insertar la expresión (cómo se mostrará),
# para ello usamos : después de la expresión y después el formato

# Por ejemplo, si queremos insertar un entero reservando un mínimo de 6 huecos (caracteres)
# usamos {expresión:6d}. La d indica que queremos mostrarlo como entero, sin decimales
print(f'El valor es {entero:6d}')
# Si queremos insertar un entero reservando un mínimo de 6 huecos (caracteres)
# y rellenar los huecos que no ocupa el número con ceros, usamos el formato 06d
print(f'El valor es {entero:06d}')
# Si reservamos menos huecos de los que ocupa el número, se usa lo que el número ocupa
print(f'El valor es {entero:2d}')


# un print sin parámetros imprime una línea en blanco
print()


# a través del formato se puede convertir la expresión, cuando es un número, a:
# binario:
print(f'El valor es {entero:b}')
# octal:
print(f'El valor es {entero:o}')
# hexadecimal:
print(f'El valor es {entero:X}')

print()


# vamos a trabajar con float (números con decimales)

# IMPORTANTE: se usa un punto para los decimales, NO coma
decimal = 3.1415926535
otro_decimal = 0.000000000012345

# por defecto se imprimen todos los decimales
print(f'El decimal es {decimal}')
# si tiene muchos decimales se usa la notación científica: https://en.wikipedia.org/wiki/Scientific_notation
print(f'El decimal es {otro_decimal}')

# se pueden indicar los decimales a usar usando el formato .nf
# donde n es el número de decimales. La f indica que queremos mostrar
# un número float, es obligatorio si queremos mostrar decimales
print(f'El decimal es {decimal:.2f}')

# se pueden combinar formatos, por ejemplo reservar 6 huecos y usar 2 decimales
print(f'El decimal es {decimal:6.2f}')


# usando una g en vez de f indicamos que se use la notación científica
print(f'El decimal es {decimal:g}')
print(f'El otro_decimal decimal es {otro_decimal:g}')

print()


# podemos usar f-string para formatear texto
cadena_de_texto = 'Lorem ipsum'

# IMPORTANTE: usamos un hashtag (#) para ver donde empieza y acaba el texto
# podemos usar cualquier texto válido fuera de los placeholders

# imprimimos un texto entre #
print(f'#{cadena_de_texto}#') 

# podemos formatear el texto indicando cuántos huecos reservar,
# dónde escribir el texto dentro de esos huecos (la alineación),
# y con qué rellenar los huecos (con qué carater)
# el formato es: relleno alineación huecos (sin espacios entre ellos)
# donde relleno es un texto, alineación es:
# < alinear a la izquierda
# ^ alinear al centro
# ^ alinear a la derecha
# y huecos es un número. Son opcionales, no tenemos que indicar todos

# por ejemplo, imprimimos dos hashtags, y en el medio reservamos
# 50 huecos, se inserta el contenido de cadena_de_texto alineado al centro
print(f'#{cadena_de_texto:^50}#')

# lo mismo, alineado a la izquierda
print(f'#{cadena_de_texto:<50}#')

# lo mismo, alineado a la derecha
print(f'#{cadena_de_texto:>50}#')

# lo mismo, alineado al centro, rellenando los huecos con *
print(f'#{cadena_de_texto:*^50}#')




