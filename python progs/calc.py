# Python program to make a simple calculator

# Addition
def Add(a, b) :
    return a + b

# Subtraction
def Sub(a, b) :
    return a - b

# Multiply
def Mul(a, b) :
    return a * b

# Divide
def Div(a, b) :
    return a / b

cont = 1

while cont == 1 :
    print("Select operation : \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
    choice = int(input("Enter choice : "))
    if choice in (1, 2, 3, 4, 5) :

        if choice == 5 :
            cont = 0
            print("Exiting !!")
            break

        x = float(input("Enter first number : "))
        y = float(input("Enter second number : "))
        
        if choice == 1 :
            z = Add(x, y)
            print(f"{x} + {y} = {z}")
        elif choice == 2 :
            z = Sub(x, y)
            print(f"{x} - {y} = {z}")
        elif choice == 3 :
            z = Mul(x, y)
            print(f"{x} * {y} = {z}")
        elif choice == 4 :
            z = Div(x, y)
            print(f"{x} / {y} = {z}")
    else :
        print("Wrong choice !")
        