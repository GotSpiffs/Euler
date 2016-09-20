from math import *

def isprime(x):
    return all(False if x % i == 0 else True for i in range(2,int(ceil(sqrt(x)))))

def factors(x):
    return [[i, x/i] for i in range(2,int(floor(sqrt(x)))) if x % i == 0]


y = [i for l in factors(600851475143) for i in l]
print max(p for p in y if isprime(p))
