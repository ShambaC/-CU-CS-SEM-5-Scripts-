dic = {1 : 'a', 2 : 'a', 4 : [1, 2], 3 : 'a'}
# dic = {1 : 'a', 2 : 'a', 4 : 'b', 3 : 'a'}
dic2 = {}

for k,v in dic.items() :
    if isinstance(v, (tuple, list, set)) :
        v = frozenset(v)
    if v in dic2.keys() :
        if isinstance(dic2[v], list) :
            tmp = dic2[v]
            tmp.append(k)
            dic2[v] = tmp
        else :
            tmp = []
            tmp.append(dic2[v])
            tmp.append(k)
            dic2[v] = tmp
    else :
        dic2[v] = k

print(dic2)