L = [1,2,3,4,5]

def recursion_sum(L):
    if len(L) == 0: return 0
    return L[0] + recursion_sum(L[1:])

print recursion_sum(L)
