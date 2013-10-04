from math import *

def estimate_pi():
    """Estimates the value of pi to a precision of 1e-15. 
    
    This method of estimation is an infinite series discovered 
    
    by the mathematician Srinivasa Ramanujan. 
    """
    k = 0
    x = 0
    #term is initialized as 1, so that it does not interfere with the
    #while loop's condition
    term = 1

    while term > 1e-15:
        num = float(factorial(4*k) * (1103 + 26390*k))
        denom = (factorial(k)**4)*(396**(4*k))
        term = (num/denom)*2*sqrt(2)/9801
        x = x + term
        k = k + 1

    print(1/x)

estimate_pi()




