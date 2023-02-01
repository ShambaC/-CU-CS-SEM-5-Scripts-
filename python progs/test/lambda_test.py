area_cube = lambda a : 6 * a * a
vol_cube = lambda a : a ** 3

area_cuboid = lambda a, b, c : 2*a*b + 2*b*c + 2*c*a
vol_cuboid = lambda a, b, c : a * b * c

side = int(input("Enter the side of the cube : "))
print(f"Area : {area_cube(side)}, Volume : {vol_cube(side)}")

l = int(input('Enter length : '))
b = int(input('Enter breadth : '))
h = int(input('Enter height : '))

print(f"Area : {area_cuboid(l, b, h)}, Volume : {vol_cuboid(l, b, h)}")