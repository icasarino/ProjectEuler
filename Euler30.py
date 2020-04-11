def unit(num):
    return len(str(num))
def exp(num,potencia):
    return num*(10**potencia)

PotenciaN = 5
Result = 0
def MaxDec():
    Max = 1
    num = Max * 9**PotenciaN
    while(Max <= unit(num)):
            Max += 1
            num = Max * 9 ** PotenciaN
    return Max - 1

MaxDec = MaxDec()
print("Cantiadd máxima de cifras", MaxDec)

for i in range(2,MaxDec*(9**PotenciaN) + 1):
    lenNum = unit(i)
    valor = 0
    for j in range(0,lenNum):
        valor += int(str(i)[j]) ** PotenciaN

    if(valor == i):
        Result += valor

print(Result)