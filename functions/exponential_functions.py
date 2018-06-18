import numpy as np

def exponential(x):
    return np.exp(x)

def logarithmic(x,b):
    if b == 'e':
        return np.log(x)
    elif b == 10:
        return np.log10(x)
    elif b == 2:
        return np.log2(x)