def forContinue():
    print('Для продолжения нажмите Enter')
    input()
    return

def createVoc(bf):
    # Выход: создание словаря из списка L пар СЛОВО_толкование слова
    forContinue()

def loadDict(pth, name):
    # Выход: чтение словаря из файла pth:\ name.
    print('loadDict')
    forContinue()

def saveDict(di, nameF):
    # Выход: запись словаря di в файл nameF.
    print('saveDict')
    forContinue()

def addDict(di):
    # Выход: добавление в словарь di пары ключ:значение)
    print('addDict')
    forContinue()

def delDict(di):
    # Выход: удаление из словаря di пары по ключу.
    print('delDict')
    forContinue()

def searchByKey(di):
    # Выход: вывод в консоль значения по ключу.
    print('searchByKey')
    forContinue()

def viewDict(di):
    # Выход: просмотр словаря di
    print('viewDict')
    forContinue()


def createVoc(bf):
    # Выход: создание словаря в двоичном файле bf из списка
    # L пар СЛОВО_толкование слова
    L = [
    ('ЖАБА', 'Сходное с лягушкой бесхвостое земноводное с бородавчатой кожей.'),
    ('ЖАБО', 'Пышная отделка у воротника из кружев или лёгкой ткани.'),
    ('ЖАБРЫ', 'Органы дыхания рыб и некоторых других водных животных.'),
    ('ЖАВЕЛЬ', 'Едкий хлористый раствор зеленовато-жёлтого цвета, употр. при белении тканей.'),
    ('ЖАВОРОНОК', 'Певчая птичка отряда воробьиных.'),
    ('ЖАДИНА', 'Жадный человек.'),
    ('ЖАДНИЧАТЬ', 'Проявлять жадность, скупиться.'),
    ('ЖАДНОСТЬ', 'Скупость, корыстолюбие.'),
    ('ЖАДНЫЙ', 'Стремящийся к наживе, скупой.'),
    ('ЖАДЮГА', 'То же, что жадина.'),
    ('ЖАЖДА', 'Потребность, желание пить.'),
    ('ЖАЖДАТЬ', 'Сильно желать.'),
    ('ЖАКАН', 'Пуля для стрельбы из гладкоствольного охотничьего ружья.'),
    ('ЖАКЕТ', 'Короткая верхняя одежда.'),
    ('ЖАЛЕЙКА', 'Народный духовой язычковый музыкальный инструмент — деревянная трубка с раструбом из коровьего рога или бересты.'),
    ('ЖАЛЕТЬ', 'Чувствовать жалость, сострадание к кому-н.')
]

    di = {}  # пустой словарь.
    for k, v in L:  # заполняем словарь.
        di[k] = v
    import pickle
    # Пишем словарь в двоичный файл:
    with open(bf, 'wb') as g:
        pickle.dump(di, g)
    g.close()


def loadDict(bf):
    # Выход: чтение словаря из двоичного файла bf.
    import os
    # Проверяем наличие двоичного файла:
    if not os.path.isfile(bf):
        print('Двоичного файла нет')
        return
    import pickle
    # Читаем словарь из файла:
    with open(bf, 'rb') as f:
        di = pickle.load(f)
    return di


def saveDict(di, bf):
    # Выход: запись словаря di в бинарный файл bf.
    import pickle
    with open(bf, 'wb') as f:
        pickle.dump(di, f)
    f.close()


def addDict(di):
    # Выход: добавление в словарь di пары ключ:значение
    print('Слово: ')
    k = input().upper()  # перевод в верхний регистр.
    print('Толкование: ', end='')
    v = input()
    di[k] = v
    return di


def delDict(di):
    # Выход: удаление из словаря di пары по ключу.
    print('Слово:')
    k = input().upper()
    if k in di.keys():
        del di[k]
    else:
        print(k, ' нет в словаре.')
    return di


def searchByKey(di):
    # Выход: вывод в консоль значения по ключу.
    print('Слово:')
    k = input().upper()
    print(di.get(k, ' нет в словаре'))


def viewDict(di):
    # Выход: просмотр словаря di
    for (k, z) in di.items():
        print(k, '\n', z)


def menu():  # Горизонтальное меню.
    bf ='/Users/daniildyatlov/develop/university/Python/lab14/dict.dat'
    di = {}
    while True:
        print(chr(27) + "[2J")  # Очистка консоли!
        print("0. Создание словаря")
        print("1. Чтение словаря")
        print("2. Сохранение словаря")
        print("3. Добавление в словарь")
        print("4. Удаление из словаря")
        print("5. Поиск по ключу")
        print("6. Просмотр словаря")
        print("7. Завершение")
        print(" Выберите номер")
        num = input()
        if num == '0':
            print('Если словарь уже был создан,')
            print(' то он будет заменён на первоначальный.')
            print('       Продолжить (0/1)?')
            ans = input()
            if ans == '1':
                createVoc(bf)
        if num == '1':
            di = loadDict(bf)
            if di is not None:
                forContinue()
        if num == '2':
            di = loadDict(bf)
            if di is not None:
                saveDict(di, bf)
                forContinue()
        if num == '3':
            di = loadDict(bf)
            if di is not None:
                addDict(di)
                saveDict(di, bf)
                forContinue()
        if num == '4':
            di = loadDict(bf)
            if di is not None:
                delDict(di)
                saveDict(di, bf)
                forContinue()
        if num == '5':
            di = loadDict(bf)
            if di is not None:
                searchByKey(di)
                forContinue()
        if num == '6':
            di = loadDict(bf)
            if di is not None:
                viewDict(di)
                forContinue()
        if num == '7':
            return


menu()
