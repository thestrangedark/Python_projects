from math import *
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    delta = (x1-x0)   # starting value of delta x
    x = x1          # Stores x1 as x
    f0= fcn(x0)      # Stores the fcn(x0) as fold for the starting point of the integration
    Niter = 0          # Sets the initial number of integrations to 0
    while Niter < maxiter and abs(delta) > xtol:         # The while loop will continue to loop until the condition is no longer true
        f1 = fcn(x)                                       # Calculates the value of f(x) and stores it as f1
        delta = -f1/((f1-f0)/(delta))            # Calculates the new delta x
        x += delta                                # Calculates the new x
        f0 = f1                                      # Stores the f1 -> f0
        Niter += 1                                     # iterations + 1
    return x                                            # Returns x

def main():
    fn1 = lambda x: x-3*cos(x)          # stand-alone function sent to the Secant function
    fn2 = lambda x: cos(2*x)*x**3            # same as above
    fn3 = lambda x: cos(2 * x) * x ** 3                     # same as above
    r1 = Secant(fn1, 1, 2, maxiter=5, xtol=1e-4)                 # gives the Secant function args and runs it
    r2 = Secant(fn2, 1, 2, maxiter=15, xtol=1e-8)                       # same as above
    r3 = Secant(fn3, 1, 2, maxiter=3, xtol=1e-8)                          # same as above
    print('Roots', '\nr1=', r1, '\nr2=', r2, '\nr3', r3)                  # Prints the results


main()
