#!/bin/bash
# Быстрый запуск через Docker (для macOS)

echo "Запуск через Docker..."
docker run --rm -v "$(pwd):/workspace" -w /workspace i386/ubuntu:20.04 bash -c "
    apt-get update -qq 2>/dev/null && 
    apt-get install -y -qq nasm binutils 2>/dev/null && 
    nasm -f elf32 test.asm -o test.o && 
    ld -m elf_i386 test.o -o test && 
    ./test
"

