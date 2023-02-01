import math

l = [12, 34, 56, 23, 38, 32, 59, 69, 42, 83]
size = len(l)

for i in range(size) :
    for j in range(size - i - 1) :
        if l[j] < l[j + 1] :
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp

print(f"Sorted list : {l}")

l2 = []

for x in l :
    x = math.pi * x
    x = round(x, 2)
    l2.append(x)

tup = (l2[0], l2[-2])

print(f"new list : {l2}\nNew tupple : {tup}")
