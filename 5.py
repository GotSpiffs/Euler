from math import *

k = 2520

check = True

while check:

    count = 0
    k += 2520

    for i in range(11,20):

        if k % i == 0:
            count += 1

    if count == 9:
        check = False
    
    print k

print k