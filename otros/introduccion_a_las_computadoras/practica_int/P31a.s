.data

.text
.globl main


main:

      addi $t0, $0, 5
      addi $t1, $0, -33
      add  $t2, $t0, $t1

      addi $v0, $0, 10
      syscall