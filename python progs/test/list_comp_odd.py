l = []

n = int(input("Enter the size of the list : "))
print('Enter element for list : ')

for i in range(n) :
    tmp = int(input())
    l.append(tmp)

l1 = [x for x in l if x % 2 != 0]
l2 = [x for x in l if x % 3 == 0]
print(l1)
print(l2)