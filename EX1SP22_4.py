from math import *

def GetRndInt(seeds, NLow, NHigh):
    '''
    Implementation of Wichmann-Hill pseudorandom number generator.
    Note:  a 16 bit (signed) integer can store values up to 32767.
    :param seeds: seed values to initiate the production of next generation of seed values
    :param NLow: the low limit of my range for a random number
    :param NHigh: the high limit of my range for a random number
    :return: the random number, new seed values as a tuple
    '''
    H=max(NLow,NHigh) #range check
    L=min(NLow,NHigh) #range check
    s1,s2,s3=seeds #unpack seeds
    s1= fmod((171 * s1),  30269) #$JES Missing Code$ #see Wichmann-Hill
    s2= fmod((172 * s2),  30307) #$JES Missing Code$ #see Wichmann-Hill
    s3= fmod((170 * s3),  30323) #$JES Missing Code$ #see Wichmann-Hill
    fNum= fmod#$JES Missing Code$ #see Wichmann-Hill
    fNum*= fmod#$JES Missing Code$ #the default is a random number between 0.0 and 1.0, so scale to my range
    fNum+= fmod#$JES Missing Code$ #now shift to make min val NLow
    return fNum, (s1,s2,s3)

def CheckForDuplicates(A):
    if (i not in A):
        A.append(i)
        E[i] = True
        count = count + 1
    #$JES Missing Code$
    return nDuplicates

def main():
    '''
    Produce a 10x10 matrix with integers between 0 to 100
    ensuring that none of the numbers get duplicated.
    Step 0. Write GetRnd function to generate a random integer between 0 to 100
    Step 1. Create a tuple called seeds with initial seed values.
    Step 2. Create a list (E) with integers from 0 to 100 as eligible integers
    Step 3a. Scan through all the positions in the matrix.
    Step 3b. While at each position, generate a random integer (I) between 0 to len(eligible list)
    Step 3c. Set value in A to E[I].
    Step 3d. Remove E[I] from E.
    Step 4. After the array is created, verify that no duplicates exist with CheckForDuplicates function.
    :return:
    '''
    #Step 1.
    seeds= [1234, 19857, 25000] #$JES Missing Code$ #initial seeds
    #Step 2.
    E= range[0, 100]#$JES Missing Code$ #creates the range of eligible integers
    #Step 3.
    A=if(I not in E):
            A.append(r)
            E[I] = True#$JES Missing Code$
    #step 4.
    nDup=CheckForDuplicates(A) #check for duplicates
    if nDup==0:
        #this is the desired output
        print("Verified. {:d} duplicated number!".format(nDup))
    else:
        #if I get this, something went wrong
        print("Failed. {:d} duplicated numbers".format(nDup))

main()