from numba import jit
import numpy as np
import ctypes
import timeit
import wallis_cython

###
wallislib = ctypes.CDLL('./wallis.so')
wallis__ = getattr(wallislib, 'wallis')
wallis__.restype = ctypes.c_float
def wallis_c(n):
    return wallis__(n)

### 
def wallis(n):
    pi = 2.
    for i in range(1, n):
        i_ = 4. * i**2
        pi *= i_/(i_ -1)
    return pi

@jit
def wallis_numba(n):
    pi = 2.
    for i in range(1, n):
        i_ = 4. * i**2
        pi *= i_/(i_ -1)
    return pi

def wallis_np(n):
    i = np.arange(1, n, dtype=np.float32)
    i *= i 
    i *= 4 
    return 2. * np.prod(i/(i-1))


%timeit wallis_cython.wallis(10000)
%timeit wallis_c(10000)
%timeit wallis(10000)
%timeit wallis_numba(10000)
%timeit wallis_np(10000)


