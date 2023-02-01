# WAP in python to implement all pythagorean triplet within a range by euclid formula
# It is started with a pair of positive integer m and n, where they are coprime.
# Then the formula for the triplet (a, b, c) is a^2 + b^2 = c^2,
# where a = m^2 - n^2, b = 2mn, c = m^2 + n^2


n=int(input("Enter upper limit of range : "))
print("The list of pythagorean triplets within this range : ")

for i in range(1, n - 1) :
    for j in range(i + 1, n) :
        for k in range(i + 2, n - 2) :
            a = k*k
            b = i*i + j*j
            if a == b :
                print(f"{i}, {j}, {k}")