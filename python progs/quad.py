# Root of quadratic equation

import math as m

a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))

d = b**2 - (4*a*c)

if d > 0:
    root1 = (-b + m.sqrt(d))/(2*a)
    root2 = (-b - m.sqrt(d))/(2*a)
    print('\nRoots are real and distinct\n')
    print('Root 1 : ', float(root1), 'Root 2 : ', float(root2))
elif d == 0:
    root = -b/(2*a)
    print('\nRoots are real and equal\n')
    print('Root : ', float(root))
else:
    p = -b/(2*a)
    q = m.sqrt(-d)/(2*a)
    print('\nRoots are imaginary\n')
    x = complex(p, round(q, 2))
    y = complex(p, round(-q, 2))
    print('Roots are : ', x, y)
