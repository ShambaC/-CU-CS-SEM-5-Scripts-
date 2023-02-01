# Copy contents of one file into another
# Emulate the cp command

# Open the file for reading
f1 = open("a.txt", "r")

# Open the file for writing
with open("b.txt", "w") as f2 :
    for line in f1 :
        f2.write(line)

f3 = open("b.txt", "r")
print(f3.read())