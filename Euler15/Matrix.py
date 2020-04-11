class Posicion:
	def __init__(self,i,j):
		self.i = i
		self.j = j

def createMatrix(matrix,size):
	for i in range(size):
		line = []
		line.append(0)
		for j in range(size - 1):
			line.append(0)
		matrix.append(line)

def printMatrix(matrix):
	for row in matrix:
		print(row)

def updateMatrix(matrix, pos, value):
	matrix[pos.i][pos.j] = value

def getValue(matrix, pos):
	return matrix[pos.i][pos.j]


"""
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])   

print("3rd column =", column)"""