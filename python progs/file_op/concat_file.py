# Program to concatenate the content of two files
# to emulate the cat command

data1 = data2 = ""

# Reading data from file 1
with open("a.txt", "r") as f1 :
    data1 = f1.read()

# Reading data from file 2
with open("c.txt", "r") as f2 :
    data2 = f2.read()

# Merging the content of two file
data1 += "\n"
data1 += data2

# merge file contents
with open("d.txt", "w") as f3 :
    f3.write(data1)
    print("Content of file after concatenation : \n")
    
f3 = open("d.txt", "r")
print(f3.read())