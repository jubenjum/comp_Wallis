import ctypes

###
wallislib = ctypes.CDLL('./wallis.so')
wallis__ = getattr(wallislib, 'wallis')
wallis__.restype = ctypes.c_float
def wallis_c(n):
    return wallis__(n)

n = 100000000 
print("{} -> {}".format(n, wallis_c(n)))
