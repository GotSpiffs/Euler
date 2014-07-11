from math import *


def ispalin(x):
   
    s = str(x)

    l = list(s)
    
    count = len(s) - 1
    
    t = ['l']*len(s)

    for i in l:

        t[count] = i

        count -= 1

    if t == l:

        return True
    else:
        return False


l = []

for i in range(100, 999):

    for j in range(100, 999):

        if ispalin(i*j):

            l.append(i*j)

print max(l)