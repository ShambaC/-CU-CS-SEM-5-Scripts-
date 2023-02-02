import sys

if sys.argv[1] == "^" :
    
    s = input()
    file = open(sys.argv[2], 'w')
    file.write(s)
    file.close

elif sys.argv[len(sys.argv) - 2] == "^^" :
    
    data = ""
    for i in range(1, len(sys.argv) - 2) :
        f = open(sys.argv[i])
        data += f.read() + "\n"
        f.close()
    f2 = open(sys.argv[len(sys.argv) - 1], 'w')
    f2.write(data)
    f2.close()

else :
    
    file = open(sys.argv[1], 'r')
    print(file.read())
    file.close()