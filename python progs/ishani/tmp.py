d1={1:'a',2:'a',3:'b'}
d2={}


c=0
list1=[]
for x in d1:
    list1.append([])
    list1[c].append(x)
    print(list1)

    for y in d1:
        if d1[x]==d1[y]:
                list1[c].append(y)
    
    print(list1)
    set1=set(list1[c])
    list1[c]=list(set1)
    print(list1)
    
    if(len(list1[c])>1):
        d2[d1[x]]=list1[c]
    else:
        d2[d1[x]]=x
    c+=1

print(list1)

print(d1)
print(d2)