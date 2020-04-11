
def tostring(list):
    x = ""
    for i in list:
        x += str(i)

    return x


def lexicographically_next_permutation(a):

    i = len(a) - 2
    while not (i < 0 or a[i] < a[i + 1]):
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]  # swap
    a[i + 1:] = reversed(a[i + 1:])  # reverse elements from position i+1 till the end of the sequence
    return True


li = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]
print(li)    # process
i = 2
while lexicographically_next_permutation(li):
    if i == 1000000:
        print(str(i) + " " +tostring(li))    # process
        break
    i += 1