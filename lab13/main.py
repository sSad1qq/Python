import random
import timeit


VAR = 7


A_RANGE, B_RANGE = -5 * (VAR + 1) * 100000, 5 * (VAR + 1) * 100000

N_el = (VAR + 1) * 100000


# функция для создания массива из n случайных элементов
def createArr(n):
    arr = []
    for _ in range(n):
        arr += [random.randint(A_RANGE, B_RANGE)]
    return arr


# тип узлов дерева
class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def printTree(tr, k):
    if tr.right != None:
        printTree(tr.right, k + 1)

    for _ in range(k):
        print("..", end = "")
        print(tr.data)
    
    if tr.left != None:
        printTree(tr.left, k + 1)


def addNode(tr, d):
    if tr != None:
        if d <= tr.data:
            if tr.left == None:
                tr.left = node(d)
            else:
                addNode(tr.left, d)
        elif d > tr.data:
            if tr.right == None:
                tr.right = node(d)
            else:
                addNode(tr.right, d)
    
    return tr


def createTreeFromArr(A):
    bTr = node(A[0])
    for j in range(1, len(A)):
        bTr = addNode(bTr, A[j])

    return bTr


def searchInArr(d, A):
    for j in range(len(A)):
        if A[j] == d:
            return True
    return False


def searchOnTree(d, tr):
    if tr == None:
        return False
    if tr.data == d:
        return True
    if tr.data >= d:
        return searchOnTree(d, tr.left)
    else:
        return searchOnTree(d, tr.right)


A = createArr(N_el)
bTr = createTreeFromArr(A)
print(f"Число элементов: {N_el}")
d = A[N_el - 1]
print(f"Последний элемент в массиве: {d}")
stT = timeit.default_timer()
searchInArr(d, A)
endT = timeit.default_timer()
print('Время (сек.) построения БДП из массива:','%6.3e' % (endT-stT))
stT = timeit.default_timer()
searchOnTree(d, bTr)
endT = timeit.default_timer()
print('Время (сек.) поиска', d, 'на БДП:', "%6.3e" % (endT-stT))

