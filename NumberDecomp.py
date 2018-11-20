#David Schmeling
#Decomposing numbers into perfect squares, cubes, and 4th powers
#Program takes integer value and exponent value
#Returns a set that sums to the given value

import sys
import math
import time

sopy = []

#-------------------------------------------------------

#This function takes all possible sets and lists each set 
#that adds to the specified value n recursively
def getMinSquares(squares, n, sqlist=[]):

    sums = sum(sqlist)
    #If sum is reached, add the set to the list
    if sums == n:
        sopy.append(sqlist)

    if sums >= n:
       return

    for i in range(len(squares)):
        current_square = squares[i]
        remain = squares[i+1:]
        getMinSquares(remain, n, sqlist + [current_square])

def getMinCubes(cubes, n, cubelist=[]):

    sumz = sum(cubelist)

    if sumz == n:
        sopy.append(cubelist)

    if sumz >= n:
       return

    for i in range(len(cubes)):
        current_cube = cubes[i]
        remainz = cubes[i+1:]
        getMinCubes(remainz, n, cubelist + [current_cube])

def getMinQuads(quads, n, quadlist=[]):
    sum2 = sum(quadlist)

    if sum2 == n:
        sopy.append(quadlist)

    if sum2 >= n:
        return

    for i in range(len(quads)):
        current_quad = quads[i]
        remain2 = quads[i+1:]
        getMinQuads(remain2, n, quadlist + [current_quad])

#Created my own cube root and quad root function to 
#calculate a range of perfect squares, cubes, etc.
def cube_root(n):
    return n ** (1./3)

def quad_root(n):
    return n ** (1./4)  

#This is where the program starts by prompting the user
print("\nPlease enter an integer and the exponent value:")

for s in sys.stdin:
    val, exp = s.strip().split()
    val = int(val)
    exp = int(exp)

    #Same idea as my other function, pick the exponent and do calculations
    if exp == 2:
        #Same way to find set of all perfect squares in the range
        allsquares = [i * i for i in range(1, math.floor(math.sqrt(val)) + 1)]
        start1 = time.time()

        #Blocking anythin 3 or under because they aren't perfect squares (besides 1)
        if val <= 3:
           sopy = []

        getMinSquares(allsquares, val)
        end1 = time.time()
        time1 = (end1 - start1)

        #This is where I distinguish a decomposition or not
        if sopy:
           sopy = sopy[-1]
	   #If sopy is populated, I take the last set in the list,
           #which hopefully is the most efficient perfect square set
           

        if not sopy:
           sopy = ["No Decomposition"]
        
    #These if-statments are very similar just different exponent values
    if exp == 3:
        allcubes = [i * i * i for i in range(1, math.floor(cube_root(val)) + 1)]
        start1 = time.time()

        if val <= 7:
            sopy = []

        getMinCubes(allcubes, val)
        end1 = time.time()

        if sopy:
            sopy = sopy[-1]

        if not sopy:
            sopy = ["No Decomposition"]

    if exp == 4:
        allquads = [i * i * i * i for i in range(1, math.floor(quad_root(val)) + 1)]
        start1 = time.time()

        if val <= 15:
            sopy = []
        getMinQuads(allquads, val)
        end1 = time.time()

        if sopy:
            sopy = sopy[-1]

        if not sopy:
            sopy = ["No Decomposition"]

    #Here is the print code when user input is accepted through the command line
    time1 = (end1 - start1)
    print("\n")
    print("N = " + str(val) + " | Exp = " + str(exp) + " | T = " + str(time1) + " | Decomp = " + str(sopy)) 
    sopy = []
