import math
x = int(input('Enter the angle in degree : '))
tol = float(input("Enter the tolerance : "))

x = x * math.pi / 180
sum = 0.0
term = x

n = 1

while abs(term) > tol :
    sum += term
    term = (term * (-x ** 2))/((2 * n) * (2 * n + 1))
    n += 1

print(f"Calculated value : {sum}")
print(f"Actual value : {math.sin(x)}")