def fibonacci(n):
    if n < 2: return 1
    return fibonacci(n-1) + fibonacci(n-2)

def n_numbers(N):
    fn = []
    for i in range(N):
        fn.append( fibonacci(i) )
    return fn

print n_numbers(10)
