#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ASCII y Unicode:

- ASCII (American Standard Code for Information Interchange) es un sistema de codificación que asigna números a caracteres comunes en inglés. Por ejemplo, 'A' es 65, 'B' es 66, etc.
- Unicode es una codificación más amplia que incluye todos los caracteres de ASCII y muchos más, como letras de otros idiomas, emojis, símbolos matemáticos, etc.
- En Python, la función `ord()` devuelve el código Unicode de un carácter, y `chr()` devuelve el carácter correspondiente a un código Unicode.
"""

# %% ord() - Convierte un carácter a su código Unicode (ASCII)

char = 'A'
code = ord(char)
print(f"ord('{char}') = {code}")  # Salida: 65

# %% chr() - Convierte un código Unicode (ASCII) a su carácter
code = 66
char = chr(code)
print(f"chr({code}) = '{char}'")  # Salida: 'B'

# %% Extra: Ciclo completo de ida y vuelta

original = 'C'
code = ord(original)
converted_back = chr(code)
print(f"Original: {original}, Código: {
      code}, De vuelta a carácter: {converted_back}")

# %% Ejemplos con Unicode más allá de ASCII

letra_griega = 'Ω'         # Letra griega
emoji = '😊'               # Emoji
print(f"'Ω' → {ord(letra_griega)}")
print(f"'😊' → {ord(emoji)}")

# %% Bucle: Imprimir caracteres en un rango Unicode

inicio = ord('A')  # o 128512 para emojis
fin = ord('Z')     # o 128591 para emojis

for code in range(inicio, fin + 1):
    print(f"{code}: {chr(code)}")

# %% Bucle doble: Imprimir caracteres en un rango Unicode en columnas

inicio = ord('A')   # o 128512 para emojis
fin = ord('Z')      # o 128591 para emojis
columnas = 5

actual = inicio
while actual <= fin:
    for _ in range(columnas):
        if actual > fin:
            break
        print(f"{actual}: {chr(actual)}", end='\t')
        actual += 1
    print()
