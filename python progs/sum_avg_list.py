# Program in python to find the sum and average of a list of number

size = int(input('Enter the number of elements : '))
#list_num = []

print('Enter ', size, ' elements : ')

#for i in range(size):
    #data = int(input())
    #list_num.append(data)

list_num = list(map(int, input().split(' ')))
sum = 0

for i in list_num:
    sum += i
avg = sum/size

print('Sum = ', sum)
print('Avg = ', avg)