tup = ('A', 'A', 'B', 'C', 'C', 'C', 'D', 'D')
dic = {}
list1 = []

for x in tup :
    if x not in (list1) :
        list1.append(x)
        dic[x] = 1
    else :
        dic[x] += 1

print("The frequency Distribution is : ")
print(dic)