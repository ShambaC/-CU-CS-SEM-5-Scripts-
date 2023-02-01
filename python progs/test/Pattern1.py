l = 1
for i in range(1, 5) :
    for k in range(1, 5 - i) :
        print(' ', end=' ')
    for j in range(l) :
        if j % 2 == 0 :
            print("*", end=' ')
        else :
            print(" ", end=' ')
    print('')
    l += 2