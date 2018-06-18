import functions.arithmetic_functions as afun
import functions.polynomial_functions as pfun
import functions.exponential_functions as efun

x = 2.0
y = 5.0

# Test arithmetic functions
u = afun.addition(x,y)
print(u)

# Test polynomial functions
v = pfun.poly(y,2)
print(v)

# Test exponential functions
w = efun.exponential(x)
print(w)