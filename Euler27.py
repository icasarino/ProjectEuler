import math

def cuadratic(a, b, n):
    return pow(n, 2) + a*n + b

def prime(x):

    root = math.sqrt(abss(x))
    rounded = round(root)

    if root > rounded: rounded += 1

    for i in range(2, rounded):
        if x % i == 0:
            return False
    return True


def abss(x):
    if x < 0: return -x
    return x


tmplist = []
reslist = (0,0)


for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        n = 0
        res = cuadratic(a, b, n)
        while prime(res):
            tmplist.append(res)
            n += 1
            res = cuadratic(a, b, n)

        if reslist[0] < len(tmplist):
            reslist = (len(tmplist) - 1, a*b)
        tmplist = []


print(reslist)