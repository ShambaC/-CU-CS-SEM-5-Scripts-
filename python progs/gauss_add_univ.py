n = int(input("Enter the amount of numbers to be added : "))
l = []

print('Enter the numbers one after the other : ')
for i in range(0, n) :
    temp = int(input())
    l.append(temp)

sum = 0
i = 0
k = n - 1

while i <= k :
    if i != k :
        print(f"After sum {i + 1} : {l[i]} + {l[k]} = {l[i] + l[k]}")
        sum = sum + l[i] + l[k]
    else :
        print(f"Last digit to the sum {l[i]}")
        sum = sum + l[i]
    i = i + 1
    k = k - 1

print(f"Sum : {sum}")