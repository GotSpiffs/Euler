import time




def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        y = fib(x - 1) + fib(x - 2)

    return y

l = []

check = True
r = 3

while check:
    
    y = fib(r)
        
    if y > 4000000:
        check = False
    elif y % 2 == 0:
        l.append(y)

    r += 1

print sum(l)