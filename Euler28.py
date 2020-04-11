import numpy as np

COL_ROW = 7


lista = []
N = pow(COL_ROW, 2)

for i in range(COL_ROW):
    tmplist = []
    for j in range(COL_ROW):
        tmplist.append(0)
    lista.append(tmplist)

i = 0
j = COL_ROW - 1

lista[i][j] = N


def imprimir():
    for x in lista:
        print(x)
    print("-------------------------")


def fulllist():
    for x in range(COL_ROW - 1):
        for y in range(COL_ROW - 1):
            if lista[x][y] == 0: return False

    return True


def actualizar(valor, x, y):

    if fulllist(): return

    while y > 0 and lista[x][y - 1] == 0:
        valor -= 1
        lista[x][y - 1] = valor
        y -= 1

    while x < COL_ROW - 1 and lista[x + 1][y] == 0:
        valor -= 1
        lista[x + 1][y] = valor
        x += 1

    while y < COL_ROW - 1 and lista[x][y + 1] == 0:
        valor -= 1
        lista[x][y + 1] = valor
        y += 1

    while x > 0 and lista[x - 1][y] == 0:
        valor -= 1
        lista[x - 1][y] = valor
        x -= 1

    actualizar(valor, x, y)


def sumDiagonals():
    res = 0
    for x in range(COL_ROW):
        for y in range(COL_ROW):
            if x + y == COL_ROW - 1 or x == y:
                res += lista[x][y]
    return res


actualizar(N, i, j)
print(sumDiagonals())
#imprimir()










