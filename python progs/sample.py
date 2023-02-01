import sys

print('Hello World')
print(sys.argv[1])

pi = 3.14
radius = int(sys.argv[1])
area = pi * (radius ** 2)

print('Area = ', area)

radius = input('Enter radius : ')
radius = int(radius)
area = pi * (radius ** 2)

print('Area = ', area)