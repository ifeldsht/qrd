L = [1,2,3,4,5]
n = len(L)

for i in range(n/2):
    L[n-1-i],L[i] = L[i],L[n-1-i]
print L

