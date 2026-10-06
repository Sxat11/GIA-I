# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 08:42:54 2026

@author: Manuel Hay
"""
# Ejercicio 1
# nombre = input("Introduzca su nombre: ")
# edad = input("Introduzca su edad: ")
# print(f'¡Buenos días {nombre}, disfrute de sus {edad} años!')

# Ejercicio 2
# nombre = input('Dime tu nombre: ')
# apellido= input('Dime tu primer apellido: ')
# edad = int(input('Dime tu edad: '))
# jubliacion = 67
# anos_restantes = 67 - edad
# print(f' Sr/Sra. {apellido}, le faltan aún {anos_restantes} años para jubilarse ')

# Ejercicio 3
# base = int(input("Dime la base de un triángulo: "))
# altura = int(input("Dime la altura de un triangulo: "))
# superficie = (base * altura)/2
# print(f'La superficie del triángulo de base {base:.2f} y altura {altura:.2f} es de {superficie:.1f}')

# Ejercicio 4
# base = int(input("Dime la base de un rectángulo: "))
# altura= int(input("Dime la altura de un rectángulo: "))
# perimetro = 2*altura + 2*base
# print(f'El perímetro del rectángulo de base {base:2.2f} y altura {altura:2.2f} es de perimetro {perimetro:2.2f} ')

# Ejercicio 5
# base = int(input("Dime la base de un rectángulo: "))
# altura= int(input("Dime la altura de un rectángulo: "))
# superficie = base * altura
# print(f'El perímetro del rectángulo de base {base:2.2f} y altura {altura:2.2f} es de superficie {superficie:2.2f} ')

# Ejercicio 6 
# import math as m
# radio = int(input('Dime el radio de una esfera: '))
# area = 4 * m.pi * m.pow(radio, 2)
# volumen = (4/3)*m.pi* m.pow(radio,3)
# print(f'El area de una esfera es: {area}')
# print(f'El volumen de una esfera es: {volumen} ')

# Ejercicio 7 
# precioB = int(input("Dime el precio de un producto sin IVA: "))
# precioIVA = precioB + precioB *0.24
# print(f'Precio del producto (sin IVA): {precioB} €')
# print(f'El importe total (IVA incluido) es de {precioIVA} € ')

# Ejercicio 8 
# nombre = input('Introduzca su nombre: ')
# edad = input('Introduzca su edad: ')
# gastos_cervezas= int(input('Introduzca el total de sus gastos semanales en cervezas: '))
# gastos_transporte = int(input(('Introduzca el total de sus gastos semanales en transporte: ')))
# gastos_totales = gastos_cervezas + gastos_transporte
# print(f'Nombre: {nombre}')
# print(f'Edad: {edad}')
# print(f'Gasto semanal en cervezas: {gastos_cervezas}€')
# print(f'Gasto semanal en transporte: {gastos_transporte}€')
# print(f'Total de gastos semanales: {gastos_totales}€')

# Ejercicio 9
# nombre = input('Introduzca su nombre: ')
# edad = int(input('Introduzca su edad: '))
# n_hijos = int(input('Introduzca su número de hijos: '))
# s_anual = int(input('Introduzca su sueldo anual: '))
# s_mensual = s_anual / 14
# print(f'Nombre: {nombre}')
# print(f'Edad: {edad}')
# print(f'Número de hijos: {n_hijos}')
# print(f'Sueldo mensual: {s_mensual:.2f}')

# Ejercicio 10 
# print('Datos primer vector: ')
# a1 = int(input('Primera cordenada: '))
# a2 = int(input('Segunda cordenada: '))
# a3 = int(input('Tercera cordenada: '))
# print('Datos segundo vector: ')
# b1 = int(input('Primera cordenada: '))
# b2 = int(input('Segunda cordenada: '))
# b3 = int(input('Tercera cordenada: '))
# producto_escalar = (a1*b1) + (a2*b2) + (a3*b3)
# print(f'producto escalar: {producto_escalar} ')

# Ejercicio 11
# segundosT = int(input('Tiempo en segundos: '))
# horas= int(segundosT/3600)
# minutos = int(segundosT/60 - horas*60)
# segundos = int(segundosT - horas*3600 - minutos*60)
# print(f'{segundosT} son: {horas:2.0f}h:{minutos:2.0f}m:{segundos:2.0f}:s')

# Ejercicio 12
# print("1")
# print(f'{2:<7} {3:<7}')
# print(f'{4:<7} {5:<7} {6:<7}')
# print(f'{7:<7} {8:<7} {9:<7} {10:<7}')
# print(f'{11:<7} {12:<7} {13:<7} {14:<7} {15:<7}')

# Ejercicio 13 Revisar
# import math as m
# print('Me vas a dar 3 radios para 3 circulos')
# r1 = int(input('Radio 1: '))
# r2 = int(input('Radio 2: '))
# r3 = int(input('Radio 3: '))
# print(f'{'RADIO':<8}{'PERIMETRO':<12}{'AREA':<6}')
# print(f'{'=====':<8}{'=========':<12}{'====':<6}')
# p1 = (2*r1*m.pi)
# p2 = (2*r2*m.pi)
# p3 = (2*r3*m.pi)
# a1 = (m.pi*pow(r1,2))
# a2 = (m.pi*pow(r2,2))
# a3 = (m.pi*pow(r3,2))
# print(f'{r1:<8}{p1:<12.2f}{a1:<6.2f}')
# print(f'{r2:<8}{p2:<12.2f}{a2:<6.2f}')
# print(f'{r3:<8}{p3:<12.2f}{a3:<6.2f}')

# Ejercicio 14
# ciudad = input('Introduzca el nombre de su ciudad: ')
# maxi = int(input('Introduzca la temperatura máxima en grados Fahrenheit: '))
# mini = int(input('Introduzca la temperatura mínima en grados Fahrenheit: '))

# print(f"-------------------- {ciudad} time --------------------")
# print(f'{'T Max (ºF)':<10} {'T Min (ºF)':<10} {'T Max (ºC)':<10} {'T Min (ºC)':<10}')
# print(f'{maxi} ºF:<10 {mini} ºF:<10 ')
# print('---------------------------------------------------------') #PREGUNTAR EN CLASE

# Ejercicio 15
# T = int(input('¿Cuantos kilogramos de baldosas puede llevar el camión? '))
# B = int(input('¿Cuanto pesa cada baldosa? '))
# R = int(T/B)
# print(f'El camión puede llevar: {R} baldosas')

# Ejercicio 16 y 17
# print('Sumador de Matrices (2x2)')
# print('Datos matriz A: ')
# a11 = int(input('Dime el valor a11: '))
# a12 = int(input('Dime el valor a12: '))
# a21 = int(input('Dime el valor a21: '))
# a22 = int(input('Dime el valor a22: '))
# print('Datos matriz B: ')
# b11 = int(input('Dime el valor b11: '))
# b12 = int(input('Dime el valor b12: '))
# b21 = int(input('Dime el valor b21: '))
# b22 = int(input('Dime el valor b22: '))
# c11 = a11+b11
# c12 = a12+b12
# c21 = a21+b21
# c22 = a22+b22
# print(f'( {a11} {a12} ) \t  ( {b11} {b12} ) \t  ( {c11} {c12} )')
# print("\t    +  \t       =")
# print(f"( {a21} {a22} ) \t  ( {b21} {b22} ) \t  ( {c21} {c22} )")

# Ejercicio 18
nombre = input('Dime tu nombre: ')
apellido = input('Dime tu apellido: ')
s_mes = int(input("Dime tu sueldo mensual: "))
d_ocio= int(input("¿Cuanto gastas cada día en ocio? "))
d_comida = int(input("¿Cuanto gastas cada día en comida? "))
d_transporte = int(input("¿Cuanto gastas cada día en transporte? "))
p_ocio = int(((d_ocio * 7)/(s_mes/4))*100)
p_comida = int(((d_comida * 7)/(s_mes/4))*100)
p_transporte = int(((d_transporte * 7)/(s_mes/4))*100) 
g_semanal = int(d_ocio*7 +d_comida * 7 + d_transporte * 7)
print("*********************************************") 
print(f"****           {nombre} {apellido}         ****") 
print("% Ocio    % Comida    % Transporte    % Otros") 
print(f"  {p_ocio:.2f}%      {p_comida:.2f}%          {p_transporte:.2f}%          ???%") 
print("****                                     ****") 
print("                                Gasto semanal") 
print(f"                                      {g_semanal}€")





