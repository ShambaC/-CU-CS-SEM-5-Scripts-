n = int(input("Enter number of lines : "))
coeff = 1

for i in range(n) :
    for k in range(n - i + 1) :
        print(" ", end='')
    
    for j in range(i + 1) :
        if j == 0 or i == 0 :
            coeff = 1
        else :
            coeff = coeff * (i -j + 1) / j
        print(int(coeff), end=' ')
    print()