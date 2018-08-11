L = [1,2,3,4,5]
n = len(L)

R = [0]*n
for i in range(n):
    R[n-1-i] = L[i]
print R

# or

R = []
for i in range(n):
    R.append(L[n-1-i]) 
print R

