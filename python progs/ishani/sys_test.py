import sys
 
#reading input 
for line in sys.stdin:
    if line == "q\n" :
        break
    print(f"Input:{line}")

#displaying output
sys.stdout.write("This is the output")

#Command line arguments
print("File name:",sys.argv[0])

#System exit with message
if(int(sys.argv[3])<18):
    sys.exit("Invalid age!")
else:
    sys.exit("Valid age")