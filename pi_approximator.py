#-----------------------------
# Pi Approximator
# Emrys Halbertsma, 28/02/2020
# Uses nothing but a uniform random number generator to approximate pi
#-----------------------------

# import statements
import numpy.random as rd
from numpy import zeros
from numpy import sum

# declare parameters
n = 10
points = 1000000

# declare storage variables
pis = zeros((n,1))

for i in range(n): # independently approximate n number of pi_hats
    circle = 0
    for i in range(points): # number of darts to throw
        a,b=rd.random(),rd.random() # throw point at the dartboard uniformly
        if a**2+b**2<=1: # if the distance from the origin is greater than 1, it is by defn outside the circle
            circle+=1 # counts the number of points inside the circle
    pi_hat = 4*circle/points # number of points in the first quarter circle/number of points in the square gives pi_hat
    pis[i] =  (pi_hat) # add pi_hat to the list of pi's

print(sum(pis)/n) # average value of pi
