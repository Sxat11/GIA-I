.data
    enteros: .word 8, -7, 4096, -1024
    flotantes: .float 7.5, 5.3
    dobles: .double -0.2
    texto: .asciiz "Hola mundo!"

.text
.globl main
main:
    addi $v0, $0, 10
    syscall