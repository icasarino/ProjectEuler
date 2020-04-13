array = []
def calcVal(a,b):
    if str(i)[0] == str(j)[0]:
        return int(str(i)[1]) / int(str(j)[1])
    if str(i)[0] == str(j)[1]:
        return int(str(i)[1]) / int(str(j)[0])
    if str(i)[1] == str(j)[0]:
        return int(str(i)[0]) / int(str(j)[1])
    if str(i)[1] == str(j)[1]:
        return int(str(i)[0]) / int(str(j)[0])


for i in range(10,100):
    for j in range(10,100):
        if (str(i)[0] in str(j) or str(i)[1] in str(j)) and i != j and i % 10 != 0 and j % 10 != 0 and i < j:
            if i / j == calcVal(i,j):
                array.append((i,j))


print(len(array),print(array))

#Calculo a mano de resultado --> 1/100 --> 100