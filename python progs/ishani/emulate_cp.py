import sys

def cp(file_name1,file_name2):
    file1=open(file_name1,"r")
    file2=open(file_name2,"w")

    for line in file1:
        file2.write(line)
    
    file2.close()
    file1.close()

cp(sys.argv[1],sys.argv[2])


file1=open(sys.argv[1],"r")
print(file1.read())

file2=open(sys.argv[2],"r")
print(file2.read())