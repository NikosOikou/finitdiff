import math

class CentralFiniteDifference(object):
    pass

    @classmethod

    def first_order_central(self, f, x, h):
        return (f(x+h) - f(x-h))/(2.0*h)

    def first_order_forward(self, f, x, h):
        return (f(x+2.0*h) - 2.0*f(x+h) + f(x))/h**2

print CentralFiniteDifference.second_order_central(lambda x: x**2, x=0.5, h=0.1)
