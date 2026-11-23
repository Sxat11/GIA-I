.data
numeros: .word 8, -7, 10, -12
resultado: .word 0

.text
.globl main


main:

      la $a0, numeros
      lw $t1, 0($a0)
      lw $t0, 4($a0)

      add $t2, $t0, $t1
 
      la  $a1, resultado
      sw $t2, 0($a1)

      addi $v0, $0, 10
      syscall