import numpy as np
import matplotlib.pyplot as pyplot
from scipy import linalg

def CubicSpline(x,y,slope1=0, slope2=0, Natural=True):
    '''
    I wrote this function to make a selection to use either NaturalCubicSpline or ClampedCubicSpline depending on the
    boolean Natural.
    :param x: the x values at the nodes
    :param y: the y values at the nodes
    :param slope1: the slope of g(x) at leftmost node for clamped cubic spline
    :param slope2: the slope of g(x) at the rightmost node for clamped cubic spline
    :return: the result of either NaturalCubicSpline or ClampedCubicSpline
    '''
    return NaturalCubicSpline(x,y) if Natural else ClampedCubicSpline(x,y,slope1,slope2)

def ClampedCubicSpline(x,y, slope1, slope2):
    '''
    Given a set of data points (nodes) x,y and end point slopes, approximate f(x) with g(x), where g(x) is a cubic equation.
    We note that for each interval of x_(i)<=x<=x_(i+1) or x_(i-1)<=x<=x_(i), we can find g(x_(i+1)) and g(x_(i-1)) and calculate
    derivatives and second derivatives.  Given that g(x) is cubic, the second derivatives of the cubic function will vary linearly between
    the nodes (i.e., set first and second derivatives of adjacent intervals equal at the node that joins them). Ultimately, we find a matrix
    equation [A][g'']=[b] and solve for [g''].  The end conditions matter for the solution.  If we set the second derivatives at the end
    points equal to zero, we get a natural cubic spline.  If we set the first derivatives at the end points to known values, we get
    a clamped cubic spline.
    For the detailed derivation, see NumericalMethodsTutorial.docx.
    :param x: the set of x values for the nodes
    :param y: the set of f(x) values for the nodes
    :param slope1: the slope at the left end of the data
    :param slope2: the slope at the right end of the data
    :return: the solution vector consisting of second derivatives at the nodes
    '''
    blen=len(x)
    A=np.zeros([blen,blen])
    b=np.zeros(blen)
    for i in range(blen):
        if i==0:
            dX=x[i+1]-x[i] #deltaX for i
            A[i][i]=-dX/3
            A[i][i+1]=-dX/6
            b[i]=slope1+y[i]/dX-y[i+1]/dX
        elif i==(blen-1):
            dXl=x[i]-x[i-1] #deltaX for i-1
            A[i][i]=-dX/3
            A[i][i-1]=-dX/6
            b[i]=slope2+y[i-1]/dXl-y[i]/dXl
        else:
            dX=x[i+1]-x[i] #deltaX for i
            dXl=x[i]-x[i-1] #deltaX for i-1
            dX2=dX+dXl #deltaX for i + deltaX for i-1
            mu=dXl/dX
            lam=dX2/dX
            A[i][i-1]=mu
            A[i][i]=2*lam
            A[i][i+1]=1
            b[i]=6*((y[i+1]-y[i])/dX**2+(y[i-1]-y[i])/(dXl*dX))
    ddg=linalg.solve(A,b)
    return ddg

def NaturalCubicSpline(x,y):
    '''
    Given a set of data points (nodes) x,y and end point slopes, approximate f(x) with g(x), where g(x) is a cubic equation.
    We note that for each interval of x_(i)<=x<=x_(i+1) or x_(i-1)<=x<=x_(i), we can find g(x_(i+1)) and g(x_(i-1)) and calculate
    derivatives and second derivatives.  Given that g(x) is cubic, the second derivatives of the cubic function will vary linearly between
    the nodes (i.e., set first and second derivatives of adjacent intervals equal at the node that joins them). Ultimately, we find a matrix
    equation [A][g'']=[b] and solve for [g''].  The end conditions matter for the solution.  If we set the second derivatives at the end
    points equal to zero, we get a natural cubic spline.  If we set the first derivatives at the end points to known values, we get
    a clamped cubic spline.
    For the detailed derivation, see NumericalMethodsTutorial.docx.
    :param x: the set of x values for the nodes
    :param y: the set of f(x) values for the nodes
    :return: the solution vector consisting of second derivatives at the nodes
    '''
    blen=len(x)
    A=np.zeros([blen,blen])
    b=np.zeros(blen)
    for i in range(blen):
        if i==0 or i==(blen-1):
            A[i][i]=1
            b[i]=0
        else:
            dX=x[i+1]-x[i] #deltaX for i
            dXl=x[i]-x[i-1] #deltaX for i-1
            dX2=dX+dXl #deltaX for i + deltaX for i-1
            mu=dXl/dX
            lam=dX2/dX
            A[i][i-1]=mu
            A[i][i]=2*lam
            A[i][i+1]=1
            b[i]=6*((y[i+1]-y[i])/dX**2+(y[i-1]-y[i])/(dXl*dX))
    ddg=linalg.solve(A,b)
    return ddg

def interp(x, xvals,yvals,ddg):
    '''
    This finds the interval appropriate for interpolation of g(x) using the cubic spline and then performs
    the interpolation.  The interpolation formula is given in NumericalMethodsTutorial.docx and is a function of the
    second derivatives at the nodes that bracket the value of x.  If x=one of the node values, just return the y value
    of that node.
    :param x: The x value where we want to find g(x)
    :param xvals: The values of x for the nodes.
    :param yvals: The values of y for the nodes.
    :param ddg: The set of second derivatives of g(x) at the nodes.
    :return: g(x)
    '''
    nX=len(xvals)
    for i in range(nX):
        if x<xvals[i]: #select the appropriate interval for interpolation
            i-=1
            dXf=xvals[i+1]-x #width of interval to right of x
            dXb=x-xvals[i] #width of interval to left of x
            dX=xvals[i+1]-xvals[i] #total with of interval
            fx=ddg[i]/6*((dXf**3)/dX-dX*dXf)
            fx+=ddg[i+1]/6*((dXb**3)/dX-dX*dXb)
            fx+=yvals[i]*(dXf/dX)+yvals[i+1]*(dXb/dX)
            return fx
        if x==xvals[i]: #if at a node, just return yvals[i]
            return yvals[i]

def PlotCubicSpline(x,y,slope1,slope2, showpoints=True,npoints=500):
    '''
    Step 1:  create a numpy array for the plot using linspace between min(x) to max(x).
    Step 2:  create numpy arrays for y values to plot with natural spline and clamped spline using interp function.
    Step 3:  plot the values from step 1 & 2.
    Step 4:  plot the node data
    Step 5:  label appropriately and show plot
    :param x: the x values of the nodes
    :param y: the y value of the nodes
    :param slope1: the slope of g(x) at leftmost node for clamped cubic spline
    :param slope2: the slope of g(x) at the rightmost node for clamped cubic spline
    :param showpoints:  boolean to decide if nodes should be drawn
    :param npoints:  number of points for constructing the data to plot
    :return:  nothing to return
    '''
    xcubicvals = np.linspace(x[0], x[len(x)], npoints)
    ycubicvals = []
    ddg = ClampedCubicSpline(x, y, slope1, slope2)
    for i in range(len(xcubicvals)):
        ycubicvals.append(interp(xcubicvals[i], x, y, ddg))
    xnatvals = np.linspace(x[0], x[len(x)], npoints)
    ynatvals = []
    for i in range(len(xnatvals)):
        ynatvals.append(NaturalCubicSpline(x, y))
    pyplot.plot()


def main():
    '''
    Calculates and plots natural and clamped cubic splines for x,y data (nodes).
    :return:
    '''
    x=np.array([1.5, 3, 4.5, 6,  7.5, 9]) #create an array for the x values of the data
    y=np.array([3.5, 1.5, -2, 6.9, 8.2 ,1.5]) #create an array of the y values of the data
    slp1=2 #to be used for a clamped cubic spline
    slp2=-4 #to be used for a clamped cubic spline

    PlotCubicSpline(x,y,slp1,slp2,showpoints=True)

main()