from math import *
from EX1SP22_4 import GetRndInt
from hw2a import Simpson, GNPDF
from hw2b import Secant

def Clamp(x, fLow, fHigh):
    """
    This function clamps a number between fLow and fHigh, inclusive
    :param x: the number to be clamped
    :param fLow: the low value for the range
    :param fHigh: the high value for the range
    :return: the clamped value and a boolean if the number got clamped
    """
    if x>fHigh: return fHigh,True
    if x<fLow: return fLow, True
    return x,False

def main():
    '''
    This main creates a list of uniformly, randomly distributed probabilities and finds corresponding
    values of x by integrating GNPDF between mu-5*sigma to x.
    step 1. Create seeds, mu, sigma, LowLim values
    step 2. Calculate pMin as lower limit on probabilities.
    step 3. create a lambda of p-P(x<c|N(mu,sigma)), such that picking correct c sets lambda fn to zero
    step 4. build list of random p values and use Secant method to find corresponding x.
    step 5. output lists of p and x along with estimates for mu, var, sigma for population
    :return: no return value
    '''
    #step 1.
    seeds= [1234, 19857, 25000] #$JES Missing Code$ #initial seed values for the pseudorandom number generator
    mu=175 #population mean
    sigma=15 #population standard deviation
    LowLim=mu-5*sigma #lower limit for integration of GNPDF

    #step 2.
    pMin=Simpson(GNPDF,(mu,sigma), mu-20*sigma, LowLim,npoints=100) #a lower limit for p values
    Probs=[] #an empty list for storing probability values
    X=[] #an empty list for storing x values
    p=0 #the point probability for use in lambda function

    #step 3.
    fn = lambda x: Secant(Probs, mu, sigma)#$JES Missing Code$ #callback for Secant

    #step 4.
    for i in range(1000): #I want 1000 values
        p,seeds= GetRndInt(seeds,0, 1)#$JES Missing Code$ #use random number generator to get p and new seeds
        p, oClamped= Clamp(p,pMin, 1.0)#$JES Missing Code$ #clamp p between pMin and 1.0
        if oClamped:
            pass #this was just for debugging
        Probs.append(p) #append list of probabilities
        x=Secant(#$JES Missing Code$) #find x corresponding to p
        X.append(x) #append x to X

    #step 5.
    print('P= \r\n',Probs)
    print('X= \r\n',X)
    M= fn #$JES Missing Code$ #calculate sample mean
    ss= x #$JES Missing Code$ #estimate population variance
    print('\r\nPopulation mean estimate = {:0.2f}'.format(M))
    print('Population variance estimate = {:0.2f}'.format(ss))
    print('Population standard deviation estimate = {:0.2f}'.format(ss**0.5))

main()