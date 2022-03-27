def ClampInclusive(val, minval, maxval): #return true if minval>val>maxval
    pass

def RemoveOutliers(vals, mean, stdev):
    pass

def SampleEstimators(vals): #calculate estimations of the population properties mean and stdev
    pass

def ReactionRate(T, P, EA, NStDev=2):
    pass

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