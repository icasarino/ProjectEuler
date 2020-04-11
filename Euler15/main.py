import Matrix as mModule


matrix = []
size = 4


def setHeuristic():
	for i in range(size):
		for j in range(size):
			if i == size - 1 or j == size - 1:
				pos = mModule.Posicion(i,j)
				mModule.updateMatrix(matrix,pos,1)
	newSize = size - 1
	for i in range(newSize):
		for j in range(newSize):
			pos = mModule.Posicion(newSize - i - 1, newSize - j - 1)

			pos2 = mModule.Posicion(size - i - 2, size - j - 1)
			pos3 = mModule.Posicion(size - i - 1, size - j - 2)

			value = mModule.getValue(matrix,pos2) + mModule.getValue(matrix,pos3)
			mModule.updateMatrix(matrix,pos,value)

def sumMatrix():
	res = 0
	for i in range(size):
		for j in range(size):
			pos = mModule.Posicion(i,j)
			res += mModule.getValue(matrix,pos)
	res += 1
	print("El resultado es: ", res)


mModule.createMatrix(matrix,size)
setHeuristic()
mModule.printMatrix(matrix)
sumMatrix()
