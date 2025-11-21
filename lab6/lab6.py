import random # для генерации случайных чисел
from timeit import default_timer # таймер


def create_matrix(row, col):
    # вход: два целых числа: кол-во строк и столбцов
    # выход: матрица размером a на b
    matrix = [[0 for _ in range(col)] for _ in range(row)] # объявление и инициализация массива
    return matrix


def fill_matrix(matrix, a, b):
    # вход: матрица и границы интервалов
    # выход: заполенная матрица случайными числами из интервала (a, b)
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            matrix[i][j] = random.randint(a + 1, b)

    return matrix


def multiply_matrix(A, B):
    # вход: две матрицы
    # выход: матрица - результат перемножения двух матрицы
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # объявление и инициализация двумерного массива, который будем возвращать
    result = create_matrix(rows_A, cols_B)
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def print_matrix(matrix):
    # вход: двумерный массив
    # выход: отображение двумерного массива как матрицы
    for row in matrix:
        print(' '.join(map(str, row)))


# основная часть программы
#вводим из какого диапозона будут браться числа для заполнения матриц
print("Введите границы интервала (a, b), из которого будут браться числа для заполнения матриц\n")
a, b = int(input("Введите левую границу интервала: ")), int(input("Введите правую границу интервала: "))
# запрашиваем данные для генерации матрицы
rowA, colA = int(input("Введите кол-во строк матрицы А: ")), int(input("Введите кол-во столбцов матрицы А: "))
rowB, colB = int(input("Введите кол-во строк матрицы B: ")), int(input("Введите кол-во столбцов матрицы B: "))
# создание матрицы А и B
start_time = default_timer()
A = fill_matrix(create_matrix(rowA, colA), a, b)
B = fill_matrix(create_matrix(rowB, colB), a, b)
# выводим наш результат
print_matrix(multiply_matrix(A, B))
end_time = default_timer()
print(f"Время выполнения программы: {round(end_time - start_time, 5)}")





