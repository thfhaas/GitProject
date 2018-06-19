import numpy as np

import functions.arithmetic_functions as afun
import functions.polynomial_functions as pfun

x = 2.0
y = 3.0

z = afun.addition(x,y)
print(z)

z = pfun.poly(x,y)
print(z)

z = np.zeros(10)
for k in range(10):
    z[k] = pfun.poly(x,k)

print(z)