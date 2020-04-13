def delDuplicates(vector):
    return list(dict.fromkeys(vector))

def pandigitalMult(a,b,res):
    vector = []
    for i in a:
        vector.append(i)
    for i in b:
        vector.append(i)
    for i in res:
        vector.append(i)

    if len(delDuplicates(vector)) == 9 and "0" not in vector:
        return int(res)


FinalRes = []
for a in range(1,2001):
    for b in range(1,5001):
        res = a * b
        if len(str(a) + str(b) + str(res)) == 9:
            aux = pandigitalMult(str(a),str(b),str(res))
            if aux != None:
                FinalRes.append(aux)

FinalVector = delDuplicates(FinalRes)
print(len(FinalVector),sum(FinalVector))