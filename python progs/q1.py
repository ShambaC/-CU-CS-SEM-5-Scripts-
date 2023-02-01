import math

l = []

n = int(input("Enter the number of elements to be inserted : "))

print("Enter the elemets one by one : ")
for i in range(n) :
    temp = int(input())
    l.append(temp)

l2 = []

for x in l :
    if x > 0 :
        temp = math.sqrt(x)
        l2.append(temp)

print(f"New list : {l2}\nSum of new list : {sum(l2)}")