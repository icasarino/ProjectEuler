#mylist = list(dict.fromkeys(mylist))




MIN = 2
MAX = 101

out = []

for a in range(MIN,MAX):
    for b in range(MIN,MAX):
        out.append(pow(a, b))


out = list(dict.fromkeys(out))

print(len(out))