import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def ff(Re, rr, CBEQN=False):
    """
    This function calculates the friction factor for a pipe based on input Re and relative roughness.
    The calculation method is selected using the CBEQN boolean.
    :param Re: the Reynolds number under question.
    :param rr: the relative pipe roughness (expect between 0 and 0.05)
    :param CBEQN:  boolean to indicate if I should use Colebrook (True) or laminar equation
    :return: the (Darcy) friction factor
    """
    if(CBEQN):
        # note:  in numpy log is for natural log.  log10 is log base 10.
        #$JES MISSING CODE HERE$
        LHS = 1 / (ff * .5)
        RHS = -2 * np.log10(rr / 3.7 + 2.51 / (Re * ff ** .5))
        ffc = LHS - RHS
        f = fsolve(ffc, 0.008)
        return f
    else:
        return 64/Re

def plotMoody():
    """
    This function produces the Moody diagram for a Re range from 1 to 10^8 and
    for relative roughness from 0 to 0.05 (20 steps).  The laminar region is described
    by the simple relationship of f=64/Re whereas the turbulent region is described by
    the Colebrook equation.
    :return: just shows the plot, nothing returned
    """
    #Step 1:  create logspace arrays for ranges of Re
    ReValsCB=np.logspace(np.log10(4000.0),8,100)  # for use with Colebrook equation
    ReValsL=np.logspace(np.log10(600.0),np.log10(2000.0),20)  # for use with Laminar flow
    ReValsTrans=np.logspace(np.log10(),np.log10()) #$JES MISSING CODE HERE$  # for use with Transition range for laminar
    #Step 2:  create array for range of relative roughness
    rrVals=np.array([0,1E-6,5E-6,1E-5,5E-5,1E-4,2E-4,4E-4,6E-4,8E-4,1E-3,2E-3,4E-3,6E-3,8E-8,1.5E-2,2E-2,3E-2,4E-2,5E-2])

    #Step 2:  calculate the friction factor in the laminar range
    ffLam=np.array(#$JES MISSING CODE HERE$)
    ffTrans=np.array(#$JES MISSING CODE HERE$)

    #Step 3:  calculate friction factor values for each rr at each Re for turbulent range.
    ffCB=np.array(#$JES MISSING CODE HERE$)  #  I used nested list comprehensions

    #Step 4:  construct the plot
    plt.loglog(ff(CBEQN=False))  # plot the solid line part for f=64/Re
    plt.loglog(ff(CBEQN=False))  # plot the dashed line part for f=64/Re

    #$JES MISSING CODE HERE$  # plot the lines from Colebrook for each roughness.  Use plt.annotate to put rougness values

    plt.xlim(600,1E8)  # restrict the plot x range
    plt.ylim(0.008, 0.10)  # restrict the plot y range
    plt.xlabel("reynolds", fontsize=16)
    plt.ylabel("friction factor", fontsize=16)
    plt.text(2.5E8,0.02,"relative roughness",rotation=90, fontsize=16)  # for the text at right of graph for relative roughness
    ax = plt.gca()
    ax.tick_params(#$JES MISSING CODE HERE$)  # format tick marks
    ax.tick_params(#$JES MISSING CODE HERE$)  # format grid lines
    ax.tick_params(#$JES MISSING CODE HERE$)  # add minor tick labels to y
    ax.yaxis.set_minor_formatter(FormatStrFormatter("%.3f"))
    plt.grid(which='both')

    plt.show()
    pass

def main():
    plotMoody()

if __name__=="__main__":
    main()


    # welp this did not go well
    # don't leave for later huh