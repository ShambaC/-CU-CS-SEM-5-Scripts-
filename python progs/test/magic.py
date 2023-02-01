def magic_num(n) :
    sum = 0
    while(n != 0) :
        a = n % 10
        sum += a
        n = int(n/10)
    if sum < 10 :
        if sum == 1 :
            return True
        else :
            return False

    return magic_num(sum)

n = int(input("Enter the number to be checked : "))
res = magic_num(n)
if res :
    print("Magic number")
else :
    print("No Magic :(")
