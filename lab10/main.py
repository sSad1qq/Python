pth = '/Users/daniildyatlov/develop/university/Python/'

import os
if not os.path.exists:  os.makedirs(pth)


VAR = 7


def f_createFile(maxEl):
    f = open(pth + 'f', 'w')
    for i in range(maxEl, 0, -1):
        f.write(str(i) + '\n')
    f.close()


def len_file(name):
    g = open(pth + name, 'r')
    S = 0
    for str in g:   S += 1
    g.close()
    return S


maxEl = (VAR + 1) * 1000
f_createFile(maxEl)
print(len_file('f'))


def f_divide(k):
# Разбиение файла pth+'f' на два: pth+'f1' и pth+'f2' группами по k элементов.
    kol = len_file('f') # число элементов в файле f.
    # Открываем файл для чтения:
    f = open(pth+'f', 'r')
    # Открываем файлы для записи:
    f1 = open(pth+'f1', 'w'); f2 = open(pth+'f2', 'w')
    t = 0
    while t < kol:
        # в f1 записываем k элементов из f:
        i = 0
        while i < k and i + t < kol:
            f1.write(f.readline())
            i += 1
        t += k 
        # в f2 записываем k элементов из f:
        i = 0
        while i < k and i + t < kol:
            f2.write(f.readline())
            i += 1
        t += k
    f.close()
    f1.close()
    f2.close()


maxEl = (VAR + 1) * 1000; f_createFile(maxEl)
f_divide(3)

'''
def f1_f2_merge(k):
    # Выход: файл pth+'f' – результат слияния с сортировкой группами по k
    #              элементов из файлов pth+'f1' и pth+'f2'
    # число элементов в файлах f1 и f2
    len_f1 = len_file('f1'); len_f2 = len_file('f2') 
    # Открываем файл для записи
    f = open(pth+'f', 'w')
    # Открываем файлы для чтения
    f1 = open(pth+'f1', 'r'); f2 = open(pth+'f2', 'r')
    # читаем элементы из f1 и f2 
    a1 = int(f1.readline()); a2 = int(f2.readline())
    t1 = 0; t2 = 0
    while t1 < len_f1 and t2 < len_f2:
        i = 0; j = 0
        while i < k and j < k and t1 < len_f1 and t2 < len_f2:
            if a1 < a2:
                f.write(str(a1)+'\n')
                t1 += 1
                if t1 < len_f1: a1 = int(f1.readline())
                i += 1
            else:
                f.write(str(a2)+'\n')
                t2 += 1
                if t2 < len_f2: a2 = int(f2.readline())
                j += 1
        while i < k and t1 < len_f1:
            f.write(str(a1)+'\n')
            t1 += 1
            if t1 < len_f1: a1 = int(f1.readline())
            i += 1
        while j < k and t2 < len_f2:
            f.write(str(a2)+'\n')
            t2 += 1
            if t2 < len_f2: a2 = int(f2.readline())
            j += 1
    # дописываем «остатки» из групп по k элементов:
    while t1 < len_f1:
        f.write(str(a1)+'\n') 
        t1 += 1
        if t1 < len_f1: a1 = int(f1.readline())
    while t2 < len_f2:
        f.write(str(a2)+'\n') 
        t2 += 1
        if t2 < len_f2: a2 = int(f2.readline())
    f.close(); f1.close(); f2.close() 


maxEl = (VAR + 1) * 1000; f_createFile(maxEl)
f_divide(3)
f1_f2_merge(3)


def sort_Simple_Mergin( ):
# Выход: отсортированный по не убыванию файл pth+'f' 
#              методом простого слияния.
    kol = len_file('f')
    k = 1
    while k < kol:
        f_divide(k) # разбиваем f на f1 и f2 группами по k элементов,
        f1_f2_merge(k) # сливаем f1 и f2 группами по k с сортировкой в f.
        k *= 2


maxEl = (VAR + 1) * 1000; f_createFile(maxEl)
sort_Simple_Mergin( )


def timeSort( ):
    from time import time
    f_createFile((VAR + 1) * 1000)
    start = time(); sort_Simple_Mergin(); end = time() 
    print('Время сортировки:', round(end-start, 4),'сек')
    
timeSort( ) # в консоли: Время сортировки: 2.8639 сек
'''