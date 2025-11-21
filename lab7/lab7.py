import random as r # генерация случайных чисел


def create_Arr(n):
    # вход: кол-во элементов в массиве
    # выход: массив, заполненный случайными числами
    Arr = [] # объявление массива
    for _ in range(n):
        Arr.append(r.randint(-50, 51)) # инициализация

    return Arr


def remove_first_t(Arr, t):
    # вход: массив и число t
    # выход: массив, в котором нет первого вхождения t

    # условия выхода из рекурсии
    if Arr == []:
        return []
    if Arr[0] == t:
        return Arr[1:]
    else:
        return [Arr[0]] + remove_first_t(Arr[1:], t)


# основная программа
n = int(input("Введите кол-во элементов в одномерном массиве: "))
Arr = create_Arr(n)
t = int(input("Введите t: "))
print(f"Исходный массив\n{Arr}")
print(f"t (удаляемый элемент): {t}")
print(f"Итоговый массив, без первого вхождения t: \n{remove_first_t(Arr, t)}")