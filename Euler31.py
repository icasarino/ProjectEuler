coinvalues = [1,2,5,10,20,50,100,200]
#coinvalues = [1,2,5]
target = 200

solutions = []
for i in range(target + 1):
    solutions.append(0)

solutions[0] = 1
for i in range(len(coinvalues)):
    for j in range(coinvalues[i],target + 1):
        solutions[j] += solutions[j - coinvalues[i]];

print(solutions[target])



