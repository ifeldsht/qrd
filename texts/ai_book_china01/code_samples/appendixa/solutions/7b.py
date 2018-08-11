L = [1,2,3,4,5,6,7,8,9,10]

def odd(L):
    if len(L) < 2: return []
    return [L[1]] + odd(L[2:])

print odd(L)
