import math

def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return a/b

def power(a,b):
    return math.pow(a,b)

def uminus(a, b):
    return a * -1.0

def sine(a, b):
    return math.sin(a)

def cosine(a, b):
    return math.cos(a)

def tangent(a, b):
    if cosine(a, b) == 0:
        raise ValueError("Tangent value undefined")
    else:
        return math.tan(a)

def fact(a, b):
    if a < 0:
        raise ValueError("Cannot carry out the factorial of a negative number.")
    else:
        if (a % 1 == 0):
            return math.factorial(int(a))
        else:
            return math.gamma(a)

if __name__ == "__main__":
    pass
