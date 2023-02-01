from sys import argv

filename = argv[1]

txt = open(filename)

#displaying the file contents
print(f"Here are the contents of {filename} : ")
print(txt.read())