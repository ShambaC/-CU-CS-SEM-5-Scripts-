# Perfect numbers

def CheckPerfect(num) :
    factors = [1]
    for i in range(2, int(num/2 + 1), 1) :
        if num % i == 0 :
            factors.append(i)
    Sum = sum(factors)
    if Sum == num :
        return True
    return False

print('Perfect numbers between 1 to 1000 are : ')
for i in range(1, 1001, 1) :
    if CheckPerfect(i) :
        print(i, end=", ")