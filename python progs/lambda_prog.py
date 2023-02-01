# Lambda function

Area_sq = lambda p : p * p
Perimeter_sq = lambda p : 4 * p
Area_rec = lambda p, q : p * q
Perimeter_rec = lambda p, q : 2 * (p + q)

a = int(input('Enter the side of the square : '))
b = int(input('Enter side 1 of rectangle : '))
c = int(input('Enter side 2 of rectangle : '))

print('Area of square is : ', Area_sq(a))
print('Perimeter of square : ', Perimeter_sq(a))
print('Area of rectangle : ', Area_rec(b, c))
print('Perimeter of rectangle : ', Perimeter_rec(b, c))