from math import *

def prime(x):
    l = [2]
    
    X = 3

    while len(l) < x:

        check = True

        for i in range(2,2+int(floor(sqrt(X)))):

            if X % i == 0:
                check = False

        if check == True:
            l.append(X)
            print X

        X += 1
    print l
    return l[x-2]

print prime(10001)