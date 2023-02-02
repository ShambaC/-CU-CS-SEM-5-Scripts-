nums = [1, 2, 3, 4, 5]
sum = 0
def func(n) :
    global sum
    sum += n
    return sum

res = map(func, nums)
res = list(res)

print(res[-1])