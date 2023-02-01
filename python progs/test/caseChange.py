s1 = "Computer Science"
s2 = ""

for i in range(len(s1)) :
    if s1[i].isupper() :
        s2 += s1[i].lower()
    elif s1[i].islower() :
        s2 += s1[i].upper()
    else :
        s2 += s1[i]

print(s2)