def n_numbers(N):
    fn = [1]*N
    for i in range(2,N):
        fn[i] = fn[i-1] + fn[i-2]
    return fn

print n_numbers(10)
