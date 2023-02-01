import numpy as np

size = int(input("Enter the size of the matrices : "))
list2 = []

print('Enter data for the first matrix : ')
for i in range(size) :
    list1 = []
    for j in range(size) :
        tmp = int(input())
        list1.append(tmp)
    list2.append(list1)

arr1 = np.array(list2)

list2 = []

print('Enter data for the second matrix : ')
for i in range(size) :
    list1 = []
    for j in range(size) :
        tmp = int(input())
        list1.append(tmp)
    list2.append(list1)

arr2 = np.array(list2)

print('The sum of the matrices is : ')

arr3 = [[0 for i in range(size)] for j in range(size)]

for i in range(size) :
    for j in range(size) :
        arr3[i][j] = arr1[i][j] + arr2[i][j]

print(arr3)

print('The product of the matrices is : ')

for i in range(size) :
    for j in range(size) :
        arr3[i][j] = 0
        for k in range(size) :
            arr3[i][j] += arr1[i][k] * arr2[k][j]

print(arr3)