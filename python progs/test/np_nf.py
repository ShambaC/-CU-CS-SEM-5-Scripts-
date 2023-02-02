import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

# Fibonacci
s1 = 0
s2 = 1
series = []
while s1 <= b :
    series.append(s1)
    t = s1 + s2
    s1 = s2
    s2 = t

primes = []

for i in range(a, b+1) :
    isPrime = True
    for j in range(2, int(i/2) + 1) :
        if i % j == 0 :
            isPrime = False
            break
    if isPrime :
        primes.append(i)

ignore = []
ignore.extend(series)
ignore.extend(primes)

print("Output : ")
for i in range(a, b+1) :
    if i not in ignore :
        print(i, end=' ')