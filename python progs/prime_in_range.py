# Prime numbers within a range

lower = int(input('Enter the lower limit : '))
upper = int(input('Enter the upper limit : '))

print(f'Prime numbers between {lower} and {upper} : ')

for i in range (lower, upper+1):
    flag = 0
    for j in range(2, int(i/2)+1):
        mod_val = i % j
        if mod_val == 0 :
            flag = 1
            break
    if not flag :
        print(i, end=' ')