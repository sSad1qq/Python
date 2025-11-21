# Как запустить код на ассемблере

## Важно
Код `test.asm` написан для **Linux x86-32**. На macOS его нельзя запустить напрямую, так как:
- macOS использует другие системные вызовы (не `int 0x80`)
- macOS по умолчанию 64-bit

## Варианты запуска

### Вариант 1: Linux (нативная сборка)

1. **Установите NASM:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install nasm
   
   # Fedora
   sudo dnf install nasm
   
   # Arch Linux
   sudo pacman -S nasm
   ```

2. **Скомпилируйте и запустите:**
   ```bash
   # Компиляция в объектный файл (32-bit)
   nasm -f elf32 test.asm -o test.o
   
   # Линковка в исполняемый файл
   ld -m elf_i386 test.o -o test
   
   # Запуск
   ./test
   ```

   Или используйте скрипт:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

### Вариант 2: Docker (рекомендуется для macOS)

1. **Установите Docker** (если еще не установлен)

2. **Запустите в контейнере Linux:**
   ```bash
   # Сборка и запуск в одном контейнере
   docker run --rm -v $(pwd):/workspace -w /workspace i386/ubuntu:20.04 bash -c "
     apt-get update -qq && 
     apt-get install -y -qq nasm binutils && 
     nasm -f elf32 test.asm -o test.o && 
     ld -m elf_i386 test.o -o test && 
     ./test
   "
   ```

3. **Или создайте Dockerfile:**
   ```dockerfile
   FROM i386/ubuntu:20.04
   RUN apt-get update && apt-get install -y nasm binutils
   WORKDIR /workspace
   COPY test.asm .
   RUN nasm -f elf32 test.asm -o test.o && \
       ld -m elf_i386 test.o -o test
   CMD ["./test"]
   ```

### Вариант 3: Виртуальная машина
Используйте виртуальную машину с Linux (например, VirtualBox + Ubuntu 32-bit)

### Вариант 4: Адаптация кода для macOS (64-bit)
Если нужно запустить на macOS, код нужно переписать для 64-bit с использованием системных вызовов macOS.

## Объяснение команд

- `nasm -f elf32` - компиляция в формат ELF 32-bit
- `ld -m elf_i386` - линковка для 32-bit архитектуры
- `int 0x80` - Linux системный вызов (на macOS не работает)

## Очистка
После запуска можно удалить промежуточные файлы:
```bash
rm -f test.o test
```

