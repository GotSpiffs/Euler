from math import *
from itertools import combinations


def ispalin(x):
	return x == int(str(x)[::-1])

max(i*j for i,j in combinations(range(100,999), r=2) if ispalin(i*j))

