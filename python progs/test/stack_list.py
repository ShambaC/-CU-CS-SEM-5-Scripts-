stack = []
top = -1

size = int(input("Enter the size of the stack : "))

def push(n) :
    global top, stack, size
    if top == size - 1 :
        print("Stack overflow !")
        return
    
    top += 1
    stack.append(n)
    print(f"{n} added to the stack at position {top}")

def pop() :
    global top, stack
    if top == -1 :
        print("Underflow !")
        return
    
    n = stack.pop()
    top -= 1
    print(f"{n} popped !")

def display() :
    global top, stack
    if top == -1 :
        print("Nothing to display !")
        return

    print(stack)

cont = True
while(cont) :
    print("Operations : \n1. Push\n2. Pop\n3. Display\n4. Exit\nEnter your choice : ", end=' ')
    choice = int(input())

    if choice in (1, 2, 3, 4) :
        if choice == 1 :
            print("Enter the value to be pushed : ", end=' ')
            n = int(input())
            push(n)
        elif choice == 2 :
            pop()
        elif choice == 3 :
            display()
        elif choice == 4 :
            print("Exiting")
            cont = False
            exit(0)
    else :
        print("Wrong choice !")