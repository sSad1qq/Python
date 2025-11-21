section .data
    msg db "Hello, world!", 0Ah ; строка + символ новой строки
    len equ $ - msg              ; длина строки

section .text
    global _start

_start:
    ; вывод строки
    mov eax, 4          ; системный вызов write
    mov ebx, 1          ; файловый дескриптор stdout
    mov ecx, msg        ; адрес сообщения
    mov edx, len        ; длина сообщения
    int 0x80            ; вызов ядра

    ; выход из программы
    mov eax, 1          ; системный вызов exit
    xor ebx, ebx        ; код возврата 0
    int 0x80
