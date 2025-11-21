import math
import timeit
import sys

# Увеличиваем лимит рекурсии для больших N
sys.setrecursionlimit(5000)

# Словарь для мемоизации факториалов (из преимуществ - быстрый доступ к элементам)
known_factorial = {}


def factorial(n):
    #Вычисляет факториал числа n с мемоизацией через словарь
    if n == 0 or n == 1:
        return 1
    if n in known_factorial:  # факториал уже вычислен
        return known_factorial[n]
    known_factorial[n] = n * factorial(n - 1)  # подсчитываем
    return known_factorial[n]


def Sr(N):
    # Вход: N – число слагаемых.
    # Выход: сумма sin(1!) + sin(2!) + ... + sin(N!), вычисленная рекурсивно
    #        без применения динамического программирования
    if N == 1:
        return math.sin(1)
    # Используем периодичность sin: sin(x) = sin(x mod 2π)
    fact_n = factorial(N)
    # Приводим большое число к диапазону используя целочисленную арифметику
    two_pi = 2 * math.pi
    angle = (fact_n % (10**15)) * (two_pi / 10**15)
    return Sr(N - 1) + math.sin(angle)


def Sd(N):
    # Вход: N – число слагаемых.
    # Выход: сумма sin(1!) + sin(2!) + ... + sin(N!), вычисленная рекурсивно
    #        с применением динамического программирования (метод сверху-вниз)
    
    # Таблица для мемоизации:
    known_S = [-1] * (N + 1)  # массив уже вычисленных значений функции S
    known_S[1] = math.sin(1)  # известное (уже вычисленное) значение суммы
    
    # Вспомогательная рекурсивная функция для вычисления с мемоизацией
    def Sd_helper(n):
        if known_S[n] == -1:  # сумма ещё не подсчитана
            # Используем периодичность sin: sin(x) = sin(x mod 2π)
            fact_n = factorial(n)
            # Приводим большое число к диапазону используя целочисленную арифметику
            two_pi = 2 * math.pi
            angle = (fact_n % (10**15)) * (two_pi / 10**15)
            known_S[n] = Sd_helper(n - 1) + math.sin(angle)  # подсчитываем
        return known_S[n]  # возвращаем результат
    
    return Sd_helper(N)


# Задание 1
print("Задание 1: Вычисление суммы S = sin(1!) + sin(2!) + ... + sin(N!)")
for N in [500, 1000, 1500, 2000]:
    print('Sr(', N, ')=', round(Sr(N), 3))
    print('Sd(', N, ')=', round(Sd(N), 3))
    print()

# Задание 2
print("\nЗадание 2: Время вычисления (в сек.)\n")
for N in [500, 1000, 1500, 2000]:
    t_r = timeit.timeit("Sr(N)", setup="from __main__ import Sr, N", number=1)
    t_d = timeit.timeit('Sd(N)', setup='from __main__ import Sd, N', number=1)
    print('Sr(', N, '):', round(t_r * 1000, 3), '*E-3')
    print('Sd(', N, '):', round(t_d * 1000, 3), '*E-3')
    print()

