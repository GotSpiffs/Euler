from math import *

def isprime(x):
    for i in range(2,int(ceil(sqrt(x)))):
        if x % i == 0:
            return False
    return True

def factors(x):
    
    l = []
    
    
    for i in range(2,int(floor(sqrt(x)))):

        if x % i == 0:

            l.append(i)
            l.append(x/i)
    
    return l


y = factors(600851475143)

y.sort()

print y

t = []



for i in y:

    if isprime(i):

        t.append(i)

print t

print max(t)