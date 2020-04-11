import TriangleFromFile as tl
tvalues = tl.triangle
svalues = tl.copyMatrix(tvalues)
size = len(tvalues)

def calcular():

    for i in range(size - 1):
        llen = len(tvalues[i])
        for j in range(llen):

            valor = tvalues[i][j]

            if tvalues[i].index(valor) < llen - 1:
                valorSig = tvalues[i][j+1]
            else:
                valorSig = 0

            hijoIzq = tvalues[i + 1][j]
            hijoDer = tvalues[i + 1][j + 1]

            if valorSig >= valor:
                hijoDer += valorSig
                if hijoIzq == svalues[i + 1][j]:
                    hijoIzq += valor    
            else:
                hijoDer += valor
                if hijoIzq == svalues[i + 1][j]:
                    hijoIzq += valor

            tvalues[i + 1][j] = hijoIzq
            tvalues[i + 1][j + 1] = hijoDer

    print("Respuesta: ", max(tvalues[size-1]))     


calcular()

