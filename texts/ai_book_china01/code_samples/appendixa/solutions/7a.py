L = [1,2,3,4,5,6,7,8,9,10]

def odd(L):
    R = []
    for i in range(1,len(L),2):
        R.append(L[i])
    return R

print odd(L)
