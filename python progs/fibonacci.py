# Python program for fibonacci series for n terms

n = int(input('Enter the number of terms : '))

a = 0
b = 1
i = 1

print(f'Fibonacci Series for {n} terms : ')

while i <= n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    i += 1