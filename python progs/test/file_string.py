data = []

with open('data.txt', 'r') as file :
    data = file.read().split()


print("\nWords ending with 'on' : ")
for x in data :
    if x[-2::1] == "on" :
        print(x, end=' ')

print("\nWords ending with 2nd and 3rd letters as 'r' and 'e' : ")
for x in data :
    if len(x) > 2 :
        if x[1] == 'r' and x[2] == 'e' :
            print(x, end=' ')

print("\nWords with no vowels : ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for x in data :
    v_count = 0
    for letters in x :
        if letters in vowels :
            v_count += 1
    if v_count == 0 :
        print(x, end=' ')