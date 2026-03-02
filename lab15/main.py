class eList:
    # Тип элементов списка
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next


def genData(n, a, b):
    # Выход: неупорядоченный набор данных в виде списка
    # из n пар (k, 'Дятлов Д.А.' + 'k'), где k случайные числа из [a, b].
    from random import randint
    L = []

    for k in range(n):
        q = randint(a, b)
        L += [(q, 'Дятлов Д. А.' + str(q))]

    return L


def hashing(data, m):
    # Вход: data – непорядочный набор пар (ключ, значение),
    # m – размер хеш-таблицы (используется для вычисления индексов)
    # Выход: хеш-таблица размера m, Keys - массив ключей.
    hTable = [eList()] * m  #массив элементов типа elList
    Inds = []   #массив индексов ключей
    for (k, v) in data:
        # вставляем пару (индекс ключа, значение)
        # в начало односвязного списка, на который указывает
        # элемент массива hTable[k % m]
        k1 = k % m
        qL = eList()
        # вставляем в начало односвязного списка:
        qL.key = k1
        if k1 not in Inds: # если индекса нет в массиве индексов,
            Inds += [k1]    # добавляем его в массив.
        qL.value = v
        qL.next = hTable[k1]
        hTable[k1] = qL
        del qL  # освобождение памяти.
    return hTable, Inds


def outHt(hT, Inds):
    # Вход: hT - хеш-таблица, Inds - массив индексов ключей.
    # Выход: вывод в консоль хеш-таблицы hT.
    for k in range(len(hT)):
        if k in Inds:
            print('Индекс:', k)
        pl = hT[k]
        while pl.next != None: # пока односвязный список не пустой:
            print(pl.key,':', pl.value)
            pl = pl.next


def searchKey(m, k, hT, Inds):
    # Вход: m - размер хеш-таблицы, k - ключ,
    #       hT - хеш-таблица, Inds - массив индексов ключей.
    # Выход: вывод в консоль пар с ключом равным k .
    i = k % m # индекс ключа.
    if i not in Inds:
        print('Пар', i, ':значение нет в хеш-таблице')
        return
    print('Пары', i, ': значение')
    pL = hT[i]
    while pL.next is not None:
        print(pL.key, ':', pL.value)
        pL = pL.next
    print('\n')


# 1. Создание неупорядоченного набора из 500 + N пар (ключ, значение),
# где ключ есть случайное целое число из отрезка [N, 2000 + N],
# значение = "Дятлов Д.А."
N=7; n=500 + N; a=N; b=2000 + N;
data = genData(n, a, b)


#2. Вывод в консоль первых 3 и последних 3 пар из
#      неупорядоченного набора.
print('Первые 3 пары:')
print(data[0],'\n', data[1],'\n', data[2],'\n')
print('Последние 3 пары:')
print(data[n-3],'\n', data[n-2], '\n', data[n-1],'\n',)


# 3. Создание хеш-таблицы методом цепочек,
#      выбрав  h(k) = k mod (250 - N) в качестве индекса ключа.
m = 250 - N
hT, Inds = hashing(data, m)


# 4. Целые числа из [0, m-1], не являющиеся индексами.
for k in range(m):
    if k not in Inds: print(k, end = ' ')
print('\n')


# 5. Вывод в консоль непустых списков,
# соответствующих наименьшему и наибольшему значению индекса.
minI = min(Inds); print('Наименьший индекс =', minI)
searchKey(m, minI, hT, Inds)
maxI = max(Inds); print('Наибольший индекс =', maxI)
searchKey(m, maxI, hT, Inds)


k = 0
while k > -1:
    print('ключ:')
    k = int(input())
    if k < 0: break
    else: searchKey(m, k, hT, Inds)






