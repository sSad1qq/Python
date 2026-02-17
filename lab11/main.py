import random
from time import time


def initAr(r):
    A = [0] * r
    for i in range(r):  A[i] = [0] * r
    for i in range(r):
        for j in range(r):
            A[i][j] = round(random.uniform(-3, 2), 2)
    
    return A


def outAr(A):
    r = len(A)
    for i in range(r):
        for j in range(r):
            print("%5.2f"%A[i][j], end = '')


def split(M):
    A = B = C = D = M
    while len(A) > len(M) / 2:
        A = A[:len(A) // 2]
        B = B[:len(B) // 2]
        C = C[len(C) // 2:]
        D = D[len(D) // 2:]
    
    while len(A[0]) > len(M[0]) // 2:
        for i in range(len(A[0]) // 2):
            A[i] = A[i][:len(A[i]) // 2]
            B[i] = B[i][len(B[i]) // 2:]
            C[i] = C[i][:len(C[i]) // 2]
            D[i] = D[i][len(D[i]) // 2:]
    
    return A, B, C, D


def addMatr(A, B):
    if type(A) == float or type(A) == int: return A + B
    r = len(A[0]); D = [0]*r
    for i in range(r): D[i] = [0]*r
    for i in range(r):
        for j in range(r):
            D[i][j] += A[i][j] + B[i][j]
    return D


def subMatr(A, B):
    if type(A) == float or type(A) == int: return A - B
    r = len(A[0]); D = [0]*r
    for i in range(r): D[i] = [0]*r
    for i in range(r):
        for j in range(r):
            D[i][j] += A[i][j] - B[i][j]
    return D


def Mult_byDef(M1, M2):
    r = len(M1[0]); D = [0]*r
    for i in range(r): D[i] = [0]*r
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                D[i][j] += M1[i][k] * M2[k][j]
    return D


def algStrassen(M1, M2, N, minSize):
    if N <= minSize:  
         return Mult_byDef(M1, M2);
    A, B, C, D = split(M1)
    E, F, G, H = split(M2)
    P1 = algStrassen(A, subMatr(F, H), N/2, minSize)
    P2 = algStrassen(addMatr(A, B), H, N/2, minSize)
    P3 = algStrassen(addMatr(C, D), E, N/2, minSize)
    P4 = algStrassen(D, subMatr(G, E), N/2, minSize)
    P5 = algStrassen(addMatr(A, D), addMatr(E, H), N/2, minSize)
    P6 = algStrassen(subMatr(B, D), addMatr(G, H), N/2, minSize)
    P7 = algStrassen(subMatr(A, C), addMatr(E, F), N/2, minSize)
    С11 = addMatr(subMatr(addMatr(P5, P4), P2), P6)
    С12 = addMatr(P1, P2)
    С21 = addMatr(P3, P4)
    С22 = addMatr(subMatr(subMatr(P5, P3), P7), P1)
    r = len(С11)*2;  C = [0]*r
    for i in range(r): C[i] = [0]*r
    for i in range(len(С11)):
       for j in range(len(С11)):
          C[i][j] = С11[i][j]
          C[i][j + len(С11)] = С12[i][j]
          C[i + len(С11)][j] = С21[i][j]
          C[i + len(С11)][j+len(С11)] = С22[i][j]
    return C


N = 512; mS = 16
print('Размеры матриц:', N,'*', N)
print('Размер минимального блока разбиения:', mS)
A = initAr(N); B = initAr(N)
start = time(); Mult_byDef(A, B); end = time()
print('Время умножения матриц по определению:', round(end-start, 3),'сек.')
start = time(); algStrassen(A, B, N, mS); end = time()
print('Время умножения матриц по алгоритму Штрассена:',
round(end-start, 3),'сек.')
