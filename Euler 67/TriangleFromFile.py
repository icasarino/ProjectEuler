def copyMatrix(matrix):
    m2 = []
    for row in matrix:
        m2.append(row.copy())
    return m2


f = open("triangledata.txt","r")
contents = f.readlines()
f.close()


triangle = []
for row in contents:
    triangle.append(row.split(" ").copy())

for row in triangle:
    for i in range(len(row)):
        row[i] = int(row[i]) 

