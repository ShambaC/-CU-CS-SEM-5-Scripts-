#string methods

str1 = 'abc'
str2 = 'anata ga suki'
print('str1[1:3] = ', str1[1:3])    #output : bc
print('str2[2:5] = ', str2[2:5])    #output : ata

str3 = 'Shamba'
print(len(str3))    #output : 6

num1 = 2
num2 = 3

#f is for format
print(f"num1 : {num1}, this was displayed using curly braces")

#explicitly using the format method
print("num2 : {}, this was displayed using format method".format(num2))

formatter = "{} {} {} {}"
print(formatter.format("one", "two", 3, False))

#preformated text using tripple quotes
print("""
This is a pre formated
multiline print statement.
This should be the third line.
Lets paste some code with indentation
for i in range (1, 90):
    tup.right(1)
    tup.forward(2)
for i in range(1, 180):
    tup.right(1)
    tup.forward(1)
""")

#Using escape sequences to display quotes and go to new line
print("I\"m a ratard\nHence the spelling mistake above.")