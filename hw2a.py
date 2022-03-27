from math import *
def Probability(PDF, args, c, GT=True):
    mean, stdev = args # unpack args
    L = mean - 5*stdev # left limit
    R = c # right limit
    p = intergation(PDF, args, L, R) # call integration
    GT = False # start with false
    if GT == True: # check that x is greater than c
        return 1 - p
    if GT == False:
        return p

def GNPDF(X, mean, stdev):
    PDF = 1/(stdev*((2*pi)**.5))*e**(-.5*((X-mean)/stdev)**2)  # calculations
    return PDF

def intergation(PDF, args, L, R):
    I = 0 # start from 0
    npoints = 100  # iterations
    mean, stdev = args  # unpack args
    if (L==R): return 0  # limits can not be the same
    dx = (R-L)/(npoints-1)  # dx change in x
    I = PDF(L, mean, stdev)+PDF(R, mean, stdev)  # probability calculations
    for i in range(1, npoints - 1):  # from 1 to 99
        X = i + dx + L  # add them up
        if i % 2 > 0:  # determine 2 or 4 depending on i
            I += 4 * PDF(X, mean, stdev)
        elif i < (npoints - 1):
            I += 2 * PDF(X, mean, stdev)
    return (dx/3.0)*I  # give calculations back

def main():
    c = 1  # constant
    mean = 0  # mean
    stdev =1  # standard deviation
    args = (mean, stdev)  # pack args with mean and stdev
    P1 = Probability(GNPDF, args, c, GT=True)  # call probability
    print('(P(X{:.2f}|N({:.2f},{:.2f}))) = {:.2f}'.format(c, mean, stdev, P1))  # print calculations for P1
    mean = 175  # mean
    stdev = 3  # standard deviation
    c = mean + 2*stdev  # second constant
    args = (mean, stdev)  # pack args
    P2 = Probability(GNPDF, args, c, GT=True)  # call probability
    print('(P(X{:.2f}|N({:.2f},{:.2f}))) = {:.2f}'.format(c, mean, stdev, P2))  # print calculations for P2

main()


# please note some this is old code from the last time i took this class