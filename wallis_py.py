def wallis(n):
    pi = 2.
    for i in range(1, n):
        i_ = 4. * i**2
        pi *= i_/(i_ -1)
    return pi



n = 100000000 
print("{} -> {}".format(n, wallis(n)))


