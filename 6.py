from math import *

big = sum(i for i in range(101))
small = sum(i ** 2 for i in range(101))

print big ** 2 - small
