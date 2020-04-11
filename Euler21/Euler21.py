def divisores(num):
    numeros = list(range(1,num//2 + 1))
    return list(filter(lambda x: num % x == 0,numeros))

def amicable(num1,num2):
    return sum(divisores(num2)) == num1 and num1 != num2

def deleteDuplicates(lista):
    return list(dict.fromkeys(lista))

numerosT = list(range(1,10001))
amicableN = []


for num in numerosT:
    num2 = sum(divisores(num))
    if amicable(num, num2):
        amicableN.append(num)
        amicableN.append(num2)
        numerosT.remove(num2)

print(sum(deleteDuplicates(amicableN)))