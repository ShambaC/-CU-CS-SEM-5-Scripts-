n = int(input("Enter a positive integer : "))

factors = []

for i in range(1, n + 1) :
    if n % i == 0 :
        factors.append(i)

print(f"factors : {factors}")
max_min = (factors[0], factors[-1])
print(f"The largest and smallest factor of {n} are : {max_min}")