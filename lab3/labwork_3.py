# импорт нужных библиотек
import numpy as np
import pylab as pl


# вспомогательная алгоритм-функция
def f(n):
    prod = 1 # счетчик для произведения
    # считаем значение функции
    for el in range(1, n + 1):
        prod *= (1 + (1.5 / n)) ** n

    return prod # возвращаем результат


# главная функция
def s(p):
    sum = 0 # счетчик для суммы
    # считаем сумму элементов
    for el in range(1, p + 1):
        sum += f(el)

    return sum # возвращаем результат


# функция для отрисовки графика функций
def drawGr(g, A, B, txt):
    AB = np.arange(A, B + 1) # множество точек {A, A + 1, ..., B}
    gAB = [g(n) for n in AB] # множество точек {g(A), g(A + 1), ..., g(B)}
    pl.scatter(AB, gAB, marker='*', color='navy', label=txt) # точечный график
    pl.legend() # отображение легенды
    pl.grid() # рисуем решетку
    pl.show() # отображаем содержимое


# основная часть программы
A, B = int(input("A = ")), int(input("B = "))
drawGr(f, A, B, 'y=f(x)') # построение графика y = f(n)
A, B = int(input("A = ")), int(input("B = "))
drawGr(s, A, B, 'y=s(p)') # построение графика y = S(P)

