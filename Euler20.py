def factorial(num):
    res = 1
    for i in range(1,num + 1):
        res *= i
    return res

def sumaDigitos(num):
    res = 0
    for n in str(num):
        res += int(n)
    return res

print(sumaDigitos(factorial(100)))