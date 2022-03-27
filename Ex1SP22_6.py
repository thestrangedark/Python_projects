from math import *
from hw2a import Simpson
from hw2b import Secant

def terms(X, thrust):
    A = 32.2 * (thrust / 56000)
    B = (32.2 / 56000) * (.5 * .002377 * 1000 * .0279)
    X/((A - B) * (X**2))

def STO(thrust):
    I = 0
    L = 0
    R = 1.2 * (56000 / (.5 * .002377 * 1000 * 2.4)) ** .5
    npoints = 100
    if (L == R): return 0
    dx = (R - L) / (npoints - 1)
    I = terms(L, thrust) + terms(R, thrust)
    for i in range(1, npoints - 1):
        X = i + dx + L
        if i % 2 > 0:
            I += 4 * terms(X, thrust)
        elif i < (npoints - 1):
            I += 2 * terms(X, thrust)
    return (dx / 3.0) * I


def ThrustNeededForTakeoff(distance):
    '''
    This function uses the Secant method to find the thrust needed
    for takeoff within the given distance.
    :param distance: desired takeoff distance in ft
    :return: the thrust required in lbf
    '''
    fn = lambda t: Secant((STO(thrust) - distance), 1, 2)  # $JES Missing Code$ #callback for Secant
    thrust = 13000  # $JES Missing Code$  #calculate the thrust
    return thrust


def main():
    '''
    This main calculates:
     1. the takeoff distance for a thrust of 13000 lbf
     2. thrust needed for takeoff distance of 1500 ft
     3. thrust needed for takeoff distance of 1000 ft
    :return:
    '''
    # calculate takeoff distance for thrust of 13000 lbf
    tod = STO(13000)  # $JES Missing Code$
    # calculate thrust needed for takeoff distance of 1500 ft
    tn1 = ThrustNeededForTakeoff(1500)  # $JES Missing Code$
    # calculate thrust needed for takeoff distance of 1000 ft
    tn2 = ThrustNeededForTakeoff(1000)  # $JES Missing Code$
    print("Take-off distance for 13,000lb thrust = {:0.1f} ft".format(tod))
    print("Thrust needed to take off in 1,500 ft = {:0.2f} lb".format(tn1))
    print("Thrust needed to take off in 1,000 ft = {:0.2f} lb".format(tn2))


main()


# code used from last time i took the class
#c