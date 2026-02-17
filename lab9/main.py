from random import choice
import timeit


VAR = 7 # Номер варианта


def init_array(m):  return [n for n in range(m, 0, -1)] # Функция для инициализации массива


# Алгоритм сортировки пузырьком
def sort_bubble(array):
    again = True # флаг для продолжения сортировки
    
    while again:
        again = False
        for k in range(len(array) - 1):
            if array[k] > array[k + 1]:
                z = array[k]
                array[k] = array[k + 1]
                array[k + 1] = z
                
                again = True
    
    return array


# Алгоритм быстрой сортировки
def sort_quick(array):

    if len(array) <= 1: return array

    q = choice(array)

    less_q = [n for n in array if n < q]
    equal_q = [q] * array.count(q)
    more_q = [n for n in array if n > q]

    return sort_quick(less_q) + equal_q + sort_quick(more_q)


Arr = init_array(8 + VAR)
print('Входной массив'); print(Arr)
print('Отсортированный массив')
print('методом пузырька:')
print(sort_bubble(Arr))
print('быстрая сортировка:')
print(sort_quick(Arr))

for N in [(VAR + 1)*100, (VAR + 1)*500, (VAR + 1)*1000]:
    A = init_array(N)
    t_b = timeit.timeit("sort_bubble(A)",setup = "from __main__ import sort_bubble, A", number = 1)
    t_q = timeit.timeit('sort_quick(A)',setup = 'from __main__ import sort_quick, A', number = 1)
    print('число элементов =', N);print('время сортировки (сек.)') 
    print('  sort_bubble:', round(t_b*1000, 3), '*E-3')
    print('  sort_quick:', round(t_q*1000, 3),'*E-3')
