.data
numeros: .word 8, 7, 9, 6, 2, 3
size: .word 6
suma: .word 0

.text
.globl main

main:
  la $a0, ---	# Puntero al vector numeros
  la $a1, size		# Cargamos la direccion del tamaño
  lw ---,0(---)		# Cargamos el tamaño del vector en a1
  
  # lazo para hacer la suma
  add $t0, $0, $0		# Inicializamos $t0 a 0, para usar como sumatorio
  
lazo:
  ----					# cargamos en $t1 cada número, usando el puntero
  add $t0, $t0, $t1		# sumamos el nuevo número cargado en la instrucción anterior
  ----					# movemos el puntero para que apunte al siguiente número
  addi $a1, $a1, -1		# decrementamos el número de elementos restantes
  ---					# salto condicional, comprueba si ya se han sumado todos
  
  la $a3, suma			# cargamos la dirección donde dejar el resultado
  ---					# almacenamos el resultado en memoria
  
exit:
  addi $v0, $0, 10		# finalización del programa
  syscall
