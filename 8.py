from itertools import islice

def multiply(x):
	return reduce(lambda x, y: x*y, x)

with open('8.txt','r') as file:
    y = []
    for line in file:
        for i in list(line.strip()):
            y.append(i)

y = [int(i) for i in y]
l = [multiply(y[i:i+13]) for i in range(len(y) - 13)]

print max(l)
