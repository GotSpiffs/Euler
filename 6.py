from math import *

big = 0
small = 0

for i in range(101):

    big += i
    small += pow(i,2)

print pow(big,2) - small
