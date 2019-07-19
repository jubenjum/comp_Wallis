from numba import jit

@jit
def wallis_numba(n):
    pi = 2.
    for i in range(1, n):
        i_ = 4. * i**2
        pi *= i_/(i_ -1)
    return pi


print("{} -> {}".format(wallis_numba(100000000))


