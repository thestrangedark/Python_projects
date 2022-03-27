import HW5SP22_a as pta
import random as rnd

def ffPoint(Re, rr):
    """
    This function takes Re and rr as parameters and outputs a friction factor according to the following:
    1.  if Re>4000 use Colebrook Equation
    2.  if Re<2000 use f=64/Re
    3.  else calculate a probabilistic friction factor where the distribution has a mean midway between the prediction
        of the f=64/Re and Colebrook Equations and a standard deviation of 20% of this mean
    :param Re:  the Reynolds number
    :param rr:  the relative roughness
    :return:  the friction factor
    """
    input(Re, rr)
    pta.ff(Re,rr,True)
    # $JES MISSING CODE HERE$
    pass


def PlotPoint(Re,f):
    # $JES MISSING CODE HERE$
    pass

def main():
    # $JES MISSING CODE HERE$
    pass

if __name__=="__main__":
    main()