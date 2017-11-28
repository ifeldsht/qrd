x = 1

def f(x):
    x = 2*x
    def g(x):
        x = x+1
        return x
    return x + g(7)

print f(2)