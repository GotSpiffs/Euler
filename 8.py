



def multiply(x):

    ans = 1

    for i in x:
        ans = ans*i

    return ans




with open('8.txt','r') as file:
    y = []
    for line in file:
        nums = line.strip()
        l = list(nums)
        for i in l:
            y.append(i)

count = 0

for i in y:
    y[count] = int(i)
    count += 1

l = []

for i in range(len(y)-13):

    l.append(multiply(y[i:i+13]))

print max(l)