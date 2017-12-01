def f1(x):
    return x*2
 
def f2(x):
    return x*x
 
L = [1,2,3,4]
L1 = [f1(x) for x in L]
L2 = [f2(x) for x in L]
print L, L1, L2
 
# or the same in place:
L1 = [x*2 for x in L]
L2 = [x*x for x in L]
print L, L1, L2
