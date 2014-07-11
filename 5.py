from math import *






k = 2520

check = True

while check:

    count = 1

    for i in range(11,20):

        if k % i != 0:
            break
        
        count += 1

    if count == 20:
        
        check = False

    k += 2520

print k