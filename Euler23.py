import time

def deleteDuplicates(lista):
    return list(dict.fromkeys(lista))


def abundantNumber(num):
    divList = list(filter(lambda x: num % x == 0, range(1, num // 2 + 1)))
    return sum(divList) > num


def sumListElements(list):
    result = []
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] + list[j] < nonAbundantMax:
                result.append(list[i] + list[j])

    return result


start = time.time()

nonAbundantMax = 28123
abundantMin = 12

abundantList = list(filter(lambda x: abundantNumber(x), range(abundantMin, nonAbundantMax)))
sumAbundant = deleteDuplicates(list(filter(lambda x: x < nonAbundantMax, sumListElements(abundantList))))

allInts = list(range(nonAbundantMax))

allNonAbundantSum = sum(list(filter(lambda x: not(sumAbundant.__contains__(x)), allInts)))
print(allNonAbundantSum)

end = time. time()
print(end - start)
