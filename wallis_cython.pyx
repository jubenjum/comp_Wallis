
def wallis(n):
    cdef float pi, t_
    pi = 2.0
    for i in range(1, n):
        t_ = 4.0 * i**20
        pi *= t_/(t_-1)
    return pi
