from scipy import integrate
import math as l


def GNPDF(x, args=(0, 1)):
    '''
        This is the Gaussian Normal Probability Density Function with parameters mean (m), standard deviation (s).
        A call to GNPDF will calculate f(x)=(1/(s*sqrt(2*pi)))*exp(-0.5*((x-m)/s)**2).
    :param x: the x value of interest
    :param args: (mean, standard deviation) as a tuple
    :return: f(x)
    '''
    m, s = args  # unpack from args
    f = (1 / (s * l.sqrt(2 * l.pi))) * l.exp(-0.5 * ((x - m) / s) ** 2)  # $JES MISSING CODE HERE$# #calculate f(x)
    return f  # return f(x)


def CDF(c, args=(0, 1)):
    '''
    This function integrates the GNPDF from mu-10*sigma to x=c to yield the probability x<c.
    :param c: the upper limit for the integration
    :param args: (mean, standard deviation) as a tuple
    :return: P(x<c|N(mu, sigma))
    '''
    fn = lambda x: GNPDF(x, args)
    # $JES MISSING CODE HERE$# #WRITE A LAMBDA FUNCTION THAT CAN ACCEPT x AS AN ARGUMENT AND CALLS GNPDF(x,args)
    I, Err = integrate.quad(fn, args[0] - 10 * args[1], c)[ 0]
    # $JES MISSING CODE HERE$# #USE integrate.quad TO RETURN THE VALUE OF THE INTEGRAL AND THE ERROR
    return I


def Probability(c, args=(0, 1), GT=False):  # NOTHING NEEDS TO CHANGE HERE
    '''
    This function returns P(x<c|N(mu, sigma)) if GT=False and 1-P(x<c|N(mu, sigma)) if GT=True
    :param c: the limiting/critical value of x
    :param args: (mean, standard deviation)
    :param GT: boolean to decide which probability I want.
    :return: P(x<c|N(mu, sigma)) if GT=False and 1-P(x<c|N(mu, sigma)) if GT=True
    '''
    P = CDF(c, args)
    return 1 - P if GT else P
