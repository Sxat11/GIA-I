# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:46:37 2026

@author: m.h.
"""
# Ejercicio 1
# n = int(input('Dime un número: '))
# if n > 0:
#     print(f'{n} es un número positivo')
# elif n < 0:
#     print(f'{n} es un número negativo')
# else: 
#     print('El número es 0')

# Ejercicio 2
# n = int(input('Dime un número: '))
# if n % 2 == 0:
#     print(f'{n} es par')
# else:
#     print(f'{n} es impar')

# Ejercicio 3
# n1 = int(input('Dime un número 1: '))
# n2 = int(input('Dime un número 2: '))
# if n1 % n2 == 0:
#     print(f'{n1} es divisible entre {n2}')
# else:
#     print(f'{n1} no es divisible entre {n2}')
    
# Ejercicio 4
# n1 = int(input('Dime un número 1: '))
# n2 = int(input('Dime un número 2: '))
# n3 = int(input('Dime un número 3: '))
# if n1 > n2:
#     if n1 > n3:
#         maxi = int(n1)
#     else:
#         maxi = int(n3)
# else:
#     if n2 > n3:
#         maxi = int(n2)
#     else:
#         maxi = int(n3)
# print(f'{maxi} es el mayor número de los introducidos. ')

# Ejercicio 5
# n1 = int(input('Dime un número 1: '))
# n2 = int(input('Dime un número 2: '))
# n3 = int(input('Dime un número 3: '))
# if n1 > n2:
#     if n1 > n3:
#         p1 = int(n1)
#         if n2 > n3:
#             p2 = int(n2)
#             p3 = int(n3)
#         else:
#             p2 = int(n3)
#             p3 = int(n2)
#     else:
#         p1 = int(n3)
#         if n1 > n2:
#             p2 = int(n1)
#             p3 = int(n2)
#         else:
#             p2 = int(n2)
#             p3 = int(n1)
# else:
#     if n2 > n3:
#         p1 = int(n2)
#         if n1 > n3:
#             p2 = int(n1)
#             p3 = int(n3)
#         else:
#             p2 = int(n3)
#             p3 = int(n1)
#     else:
#         p1 = int(n3)
#         if n1 > n2:
#             p2 = int(n1)
#             p3 = int(n2)
#         else:
#             p2 = int(n2)
#             p3 = int(n1)
# print(f'El orden es: {p1}>={p2}>={p3}')

# Ejercicio 6
# import math as m
# print(' ax^2 + bx + c')
# a = int(input("Dime el a: "))
# b = int(input("Dime el b: "))
# c = int(input("Dime el c: "))
# if ((b^2 - 4*a*c) > 0):
#     sol1 = (-b + m.sqrt((b^2) - 4*a*c))/(2*a)
#     sol2 = (-b - m.sqrt((b^2) - 4*a*c))/(2*a)
#     print(f' Las soluciones son: {sol1} y {sol2}')
# elif (((b^2) - 4*a*c) == 0):
#     sol1 = (-b/2*a)
#     sol2 = (((m.sqrt(b^2-4*a*c))/(2*a)))
#     print(f'La solución real es: {sol1}')
#     print(f'La solución imaginaria es: {sol2} ')
# else:
#     sol1 = 0
#     print('La solución es 0')
    
# Ejercicio 7
# ano = int(input('Escriba el año: '))
# mes = int(input('Escriba el mes: '))
# if mes > 12 or mes < 0:
#     mes = 1
# dia = int(input('Escriba el dia: '))
# enero = 31
# if (ano % 4 == 0 and ano % 100 != 0) or ano % 400:
#     febrero = 29 + enero
# else:
#     febrero = 28 + enero  
# marzo = 31 + febrero
# abril = 30 + marzo
# mayo = 31 + abril
# junio = 30 + mayo
# julio = 31 + junio
# agosto = 31 + julio
# septiembre = 30 + agosto
# octubre = 31 + septiembre
# noviembre = 30 + octubre
# diciembre = 31 + noviembre
# if mes == 1:
#     dias = dia
# elif mes == 2:
#     dias = dia + enero
# elif mes == 3:
#     dias = dia + febrero
# elif mes == 4:
#     dias = dia + marzo
# elif mes == 5:
#     dias = dia + abril
# elif mes == 6:
#     dias = dia + mayo
# elif mes == 7:
#     dias = dia + junio
# elif mes == 8:
#     dias = dia + julio
# elif mes == 9:
#     dias = dia + agosto
# elif mes == 10:
#     dias = dia + septiembre
# elif mes == 11:
#     dias = dia + octubre
# elif mes == 12:
#     dias = dia + noviembre
# print(f"La fecha introducida corresponde al día {dias} del año {ano}")

# Ejercicio 8
# ano_n = int(input('¿Que año naciste? '))
# mes_n = int(input('¿De que mes? '))
# dia_n = int(input('¿Que día? '))
# edad = 2026 - ano_n
# mes = 9
# dia = 29
# if (mes_n > mes):
#     edad = edad-1
# elif (mes_n == mes):
#     if (dia_n > dia):
#         edad = edad - 1
# print(f'Tienes {edad} años de edad')
    
# Ejercicio 9
# sal_anual = int(input('Introduzca su salario anual bruto (en euros): '))
# hijos = int(input('Introduzca el número de hijos menores de 18 años a su cargo: ')) 
# irpf = sal_anual * 0.15
# if hijos <=5:
#     reduccion = irpf * (0.1*hijos) 
# else: 
#     reduccion = irpf * 0.5
# print(f'IRPF(15%): {irpf}')
# print(f'Reducción debida a {hijos} a cargo {reduccion}')
# print(f'Total anual a pagar: {irpf - reduccion}')
    
# Ejercicio 10
# n1 = int(input('Introduzca primer número: '))
# n2 = int(input('Introduzca segundo número:'))
# n3 = int(input('Introduzca tercer número:'))
# if n1 > n2:
#     if n1 > n3:
#         maxi = int(n1)
#     else:
#         maxi = int(n3)
# else:
#     if n2 > n3:
#         maxi = int(n2)
#     else:
#         maxi = int(n3)
        
# if n1 < n2:
#     if n1 < n3:
#         mini = int(n1)
#     else:
#         mini = int(n3)
# else:
#     if n2 < n3:
#         mini = int(n2)
#     else:
#         mini = int(n3)

# if mini <= 0: 
#     print('Error: No se admite 0 o menor')
# else: 
#     cociente = maxi / mini
#     resto = maxi % mini
#     print(f'{maxi} dividido | entre {mini}')
#     print('          ---------------')
#     print(f'R:{resto}    C:{cociente:.0f} ')

# Ejercicio 11
l1 = int(input("Introduzca la longitud del primer lado del triángulo (cm): "))  
l2 = int(input("Introduzca la longitud del segundo lado del triángulo (cm): "))  
l3 = int(input("Introduzca la longitud del tercer lado del triángulo (cm): "))  
if l1 == l2 == l3:
    print('Es un triángulo equilatero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Es un triángulo isósceles')
else:
    print('Es un triángulo escaleno')

# Ejercicio 12


    

