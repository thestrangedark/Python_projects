#the * is called a wildcard and imports all the functions from math so I can use them without typing math. each time.
from math import *

def ClampInclusive(val, minval, maxval): #return true if minval>val>maxval
    if (minval>val) or (val>maxval):
        return True
    return False

def RemoveOutliers(vals, mean, stdev):
    RefinedVals=[] #a place for the refined data to be stored (list of lists)
    RefinedRow=[] #a place to store a row of refined data
    LowVal=mean-2*stdev  #low value
    HighVal=mean+2*stdev  #high value
    for r in vals:
        RefinedRow=[] #[x for x in r if not(ClampInclusive(x,LowVal,HighVal))]
        for c in r:
            if not ClampInclusive(c,LowVal,HighVal): #ClampInclusive returns true of c not in range
                RefinedRow.append(c)
        RefinedVals.append(RefinedRow) #put the row in RefinedVals list
    return RefinedVals #return the list of lists

def SampleEstimators(vals): #calculate estimations of the population properties mean and stdev
    Sum=0
    Var=0
    N=len(vals)
    for v in vals:
        Sum+=v #adding up all the values in the row of data
    Mean=Sum/N #calculate the sample mean
    for v in vals: #calculating the sum of squares
        Var+=(v-Mean)**2
    Var=Var/N #calculating the sample variance
    StDev=(Var*N/(N-1))**0.5 #calculates square root of unbiased variance estimator

    #alternative way to do the same thing
    mean = sum(vals) / len(vals)  # short way to write the same thing
    diffsqd = [(x - mean) ** 2 for x in vals]  # list comprehension for diff squared
    var = sum(diffsqd) / N
    stdev = (N / (N - 1) * var) ** 0.5

    return [Mean, StDev]

def ReactionRate(T, P, EA, NStDev=2):
    R=8.314 #ideal gas constant
    Rates=[] #a place to store the output
    TLow=T[0]-NStDev*T[1]+273 #calculate the low temperature
    THigh=T[0]+NStDev*T[1]+273 #calculate the high temperature
    TAvg=T[0]+273 #average temperature
    Rates.append(P*exp(-EA/(R*TLow)))  #slowest rate
    Rates.append(P*exp(-EA/(R*THigh))) #fastest rate
    Rates.append(P*exp(-EA/(R*TAvg))) #average rate
    return Rates

def main():
    print('Homework 1 - SP21: An exercise in data processing.')
    # list the experimental temperatures
    TData=[]
    #experiment 1
    TData.append([174.9, 175.4, 175.7, 177.8, 178.3, 179, 176.8, 173.8, 175.1, 174.9, 179.2, 168.4, 177.1, 180.2, 177.2, 167.5, 173.4, 174.5, 178.3, 176.4, 173.6, 171.4, 174.9, 172.6, 173.8, 175, 181.6, 175.4, 173.4, 174.3])
    #experiment 2
    TData.append([177.1, 174.6, 173.7, 181.2, 176.3, 174, 175.3, 177, 171.8, 176.4, 174.6, 176.2, 174.4, 175.1, 164.8, 176.7, 177.2, 178.5, 174.4, 175.5, 178.3, 179.6, 177.2, 172.6, 175, 175.4, 176.3, 175.1, 173.3, 178.6])
    #experiment 3
    TData.append([179.3, 174, 169.1, 174.1, 176.8, 174.5, 177.2, 176.4, 174.7, 173, 175, 172.4, 177.6, 175, 174.5, 172.5, 181.5, 174.8, 179.3, 175.4, 172.4, 170.1, 170, 175.9, 178.9, 178.5, 178.1, 168.5, 178.8, 174.1])

    TAvg=175.0 #expected temperature in degrees C
    TStDev=3.0 #Expected standard deviation of temperature

    CLow=169.0 #lower limit for clamp function (test)
    CHigh=181.0 #upper limit for clamp function (test)

    #output for part a)
    print('a)')
    print('Clamp(185, {:.1f}, {:.1f})={}'.format(CLow,CHigh, ClampInclusive(185, CLow, CHigh))) #ClampInclusive should return true
    print('Clamp(165, {:.1f}, {:.1f})={}'.format(CLow,CHigh, ClampInclusive(165, CLow, CHigh))) #ClampInclusive should return true
    print('Clamp(180, {:.1f}, {:.1f})={}'.format(CLow,CHigh, ClampInclusive(180, CLow, CHigh))) #ClampInclusive should return false

    #remove outlier data from the experimentally collected temperatures
    TRefined=RemoveOutliers(TData, TAvg, TStDev)

    #output for part b)
    print('\nb)')
    i=0
    for r in TRefined:
        n=len(TData[i-1])-len(r)
        print('Experiment {:d} had {:d} outliers'.format(i+1, n))
        print('Refined experiment {:d} data ={}'.format(i+1,r))
        i+=1

    #output for part c)
    print('\nc)')
    i=0
    stats=[]
    for r in TRefined:
        stats.append(SampleEstimators(r))
        print('Experiment {:d} stats: Mean = {:.1f}, StDev = {:.1f}'.format(i+1,stats[i][0],stats[i][1]))
        i+=1

    P=11 #frequency factor
    EA=3500 #activation energy

    #output for part d
    print('\nd)')
    i=1
    for r in stats:
        rates=ReactionRate(stats[i-1],P,EA)
        print('Experiment {:d} Rates: Min = {:.2f}, Max = {:.2f}, Avg = {:.2f}'.format(i,rates[0],rates[1], rates[2]))
        i+=1

main()