s = []

with open("words.txt", 'r') as file :
    s = file.read()
s = s.split()

list2 = []
dic = {}

for x in s :
    if x not in (list2) :
        list2.append(x)
        dic[x] = 1
    else :
        dic[x] += 1

print("The frequency Distribution is : ")
print(dic)

max = 0
max_key = ''

for k, v in dic.items() :
    if v > max :
        max = v
        max_key = k

print(f"The most frequent word is '{max_key}' with {max} occurences")