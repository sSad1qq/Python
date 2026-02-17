import random

A, B = -20, 20 # границы, из которых будут выбираться случайные числа

# Объявление типа элементов односвязного списка
class eList:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


# Создание односвязного списка из n случайных целых чисел
def createRndList(n):
    d = random.randint(A, B)
    pL = eList(d)
    
    for k in range(n - 1):
        d = random.randint(A, B)
        pL = eList(d, pL)
    
    return pL


# Функция, рекурсивно проверяющая, является ли список упорядоченным по возрастанию
def sortList(head):
    if head is None or head.next is None:
        return True
    if head.data > head.next.data:
        return False
    return sortList(head.next)


# Функция вывода элемнтов списка в консоль
def printList(pL):
    if pL is None:
        print("Список пустой")
        return
    
    while pL:
        print(pL.data, end = " ")
        pL = pL.next
    print()


n = int(input("Введите кол-во элементов: "))
pL = createRndList(n)
print("Входной список:")
printList(pL)
if sortList(pL):
    print("Список упорядочен по возрастанию")
else:
    print("Список не упорядочен по возрастанию")
