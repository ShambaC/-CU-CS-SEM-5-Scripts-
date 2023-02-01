import numpy as np

def Add(a, b) :
    print("Sum : ")
    print(a + b)

def Sub(a, b) :
    print("Difference : ")
    print(a - b)

def Mul(a, b) :
    print("Product : ")
    print(a * b)

def trans(a) :
    print("Transpose : ")
    print(np.transpose(a))

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

cont = 1

while cont == 1 :
    print("The following operations are available : \n1. Addition\n2. Subtract\n3. Multiplication\n4. Transpose\n5. Exit")
    choice = int(input("Enter choice : "))
    if choice in (1, 2, 3, 4, 5) :

            if choice == 5 :
                cont = 0
                print("Exiting !!")
                break
            
            if choice == 1 :
                Add(arr1, arr2)
            elif choice == 2 :
                Sub(arr1, arr2)
            elif choice == 3 :
                Mul(arr1, arr2)
            elif choice == 4 :
                trans(arr1)
                trans(arr2)
    else :
        print("Wrong choice !")