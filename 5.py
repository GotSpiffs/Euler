from math import *

primes = (5,7,9,11,13,16,17,19)

def div(x):
	return all(True if x % i == 0 else False for i in primes)

k = 0
x = 20
while True:

	k += x 

	if div(k):
		break


print k
