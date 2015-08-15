import math

def first_order_central(self, f, x, h):
    return (f(x+h) - f(x-h))/(2.0*h)

def first_order_forward(self, f, x, h):
    return (f(x+h) - f(x))/float(h)
