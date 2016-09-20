from math import *

primes = []

def isprime(x):
	return not any(True if x % i == 0 else False for i in primes)

def prime(count):
	global primes
	k = 1
	while count:
		k += 1
		if isprime(k):
			primes.append(k)
			count -= 1
	return k

print prime(10001)
