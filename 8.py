from itertools import islice

def multiply(x):
	return reduce(lambda x, y: x*y, x)

with open('8.txt','r') as file:
	y = [int(i) for line in file for i in list(line.strip())]

max(multiply(y[i:i+13]) for i in range(len(y) - 13))
