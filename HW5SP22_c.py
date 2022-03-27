import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def ode_system(X,t,*params):  #???what is the point of * ???
    '''
    The ode system is defined in terms of state variables.
    I have as unknowns:
    x: position of the piston (This is not strictly needed unless I want to know x(t))
    xdot: velocity of the piston
    p1: pressure on right of piston
    p2: pressure on left of the piston
    For initial conditions, we see: x=x0=0, xdot=0, p1=p1_0=p_a, p2=p2_0=p_a
    :param X: The list of state variables.
    :param t: The time for this instance of the function.
    :param params: the list of physical constants for the system.
    :return: The list of derivatives of the state variables.
    '''
    #unpack the parameters
    # $JES MISSING CODE HERE$

    #calculate derivitives
    #conveniently rename the state variables
    # $JES MISSING CODE HERE$


    #use my equations from the assignment
    xddot = # $JES MISSING CODE HERE$
    p1dot = # $JES MISSING CODE HERE$
    p2dot = # $JES MISSING CODE HERE$

    #return the list of derivatives of the state variables
    return # $JES MISSING CODE HERE$

def main():
    #After some trial and error, I found all the action seems to happen in the first 0.02 seconds
    t=np.linspace(0,0.02,200)
    #myargs=(A, Cd, Ps, Pa, V, beta, rho, Kvalve, m, y)
    A = 0.0004909
    Cd = 0.6
    Ps = 14000000
    Pa = 100000
    V = 0.0001473
    beta = 2000000000
    rho = 850
    Kvalve = 0.00002
    m = 30
    y = 0.002
    myargs = (A, Cd, Ps, Pa, V, beta, rho, Kvalve, m, y)
    # several lines here to set up initial conditions corresponding to state variables
    #call odeint with ode_system as callback, initial condidions and extra arguments/parameters
    x=odeint(x=0, ẋ=0, p1=pa, p2=pa)

    #unpack result into meaningful names
    # $JES MISSING CODE HERE$

    #plot the result
    # $JES MISSING CODE HERE$

    plt.show()

if __name__="__name__":
    main()
