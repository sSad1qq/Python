#!/bin/bash
# Скрипт для сборки и запуска test.asm

# Проверка наличия nasm
if ! command -v nasm &> /dev/null; then
    echo "Ошибка: nasm не установлен"
    echo "Установите nasm:"
    echo "  Ubuntu/Debian: sudo apt-get install nasm"
    echo "  macOS: brew install nasm"
    echo "  или используйте Docker (см. инструкцию ниже)"
    exit 1
fi

# Компиляция в объектный файл (32-bit)
echo "Компиляция test.asm..."
nasm -f elf32 test.asm -o test.o

if [ $? -ne 0 ]; then
    echo "Ошибка компиляции"
    exit 1
fi

# Линковка в исполняемый файл
echo "Линковка test.o..."
ld -m elf_i386 test.o -o test

if [ $? -ne 0 ]; then
    echo "Ошибка линковки"
    exit 1
fi

# Запуск
echo "Запуск программы..."
./test

# Очистка (раскомментируйте, если нужно)
# rm -f test.o test

