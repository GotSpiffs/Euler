from math import *

t = []

for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        t.append(i)

print sum(t)