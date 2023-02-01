# USe list comprehension to find all the odd numbers and the numbers divisible by 3 from a list of numbers.

l = [1, 2, 3, 5, 7, 6, 9, 12, 15, 20]

a = [i for i in l if i % 2 != 0]
b = [i for i in l if i % 3 == 0]
print(a)
print(b)