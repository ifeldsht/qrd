L = [1,2,3,4,5,4,3]

index = 0

for i in range(len(L)):
    if L[i] > L[index]: 
        index = i

print index
