
def getSortedNames():
    f = open("names.txt","r")
    nameList = f.readlines()
    f.close()
    nameList = nameList[0].replace('"', '').replace('[', '').replace(']', '').split(',')
    nameList.sort()
    return nameList


def convertLetterToNumber(letter):
    return ord(letter) - 95 if 'a' < letter < 'z' else ord(letter) - 64


def sumLetters(name):
    return sum(list(map(lambda x: convertLetterToNumber(x), name)))


names = getSortedNames()
nameValue = list(map(lambda x: sumLetters(x) * (names.index(x) + 1), names))
result = sum(nameValue)

print(result)
