a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
try:
    c = a/b
    print(f"Divide : {c}")
except:
    print("Some error")
finally:
    print("Goodbye")