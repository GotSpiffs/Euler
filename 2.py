a = 0
b = 1

def next_fib():
	global a
	global b
	c = a + b
	a = b
	b = c
	return c

sum = 0
x = next_fib()
while x < 4000000:
    
	if x % 2 == 0:
		sum += x
	x = next_fib()

print sum
