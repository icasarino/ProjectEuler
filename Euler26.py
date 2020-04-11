from sympy import divisors, totient
def NumOfDecimals(n):
    if n==1 or n%2==0 or n%5==0: return (0,0)
    phid=divisors(totient(n))
    for m in phid:
        if (10**m - 1)%n==0: return (n,m)


max = (0,0)
for i in range(1,1001):
    num = NumOfDecimals(i)
    if(num[1] >= max[1]):
        max = num

print(max)