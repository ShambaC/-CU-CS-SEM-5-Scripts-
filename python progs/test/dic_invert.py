dic = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4}

dic2 = {v:k for k, v in dic.items()}
print(dic2)

dic3 = dict(zip(dic.values(), dic.keys()))
print(dic3)