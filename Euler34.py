def factorial(n):
    res = []
    res.append(1)
    if n == 0: return res[0]

    for i in range(1,n + 1):
        res.append(i * res[i - 1])
    return res[n]


res = []
for i in range(0,10):
    res.append(factorial(i))

def sumFactorial(n):
    strNum = str(n)
    resSum = 0
    for i in strNum:
        resSum += res[int(i)]
    return resSum

resultado = 0
for i in range(10,1000001):
    if i == sumFactorial(i):
        resultado += i

print(resultado)




