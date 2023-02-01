queue = []
front = rear = -1

size = int(input("Enter the size of the queue : "))

def push(n) :
    global queue, front, rear, size

    if rear - front == size -1 :
        print('OVERFLOW !')
        return
    
    if front == -1 :
        front = 0

    queue.append(n)
    rear += 1

    print(f"{n} added to the stack at position {rear}")

def pop() :
    global queue, front, rear

    if rear == -1 :
        print('UNDERFLOW !')
        return

    n = queue.pop(0)
    front += 1
    if front > rear :
        front = rear = -1
    
    print(f"{n} popped !")

def display() :
    global queue, front, rear

    if rear == -1 :
        print('Nothing to show')
        return
    
    print(queue)

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