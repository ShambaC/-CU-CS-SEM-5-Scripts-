with open("a.txt", 'r') as file :

    # Counting words
    var1 = file.read()
    var1 = var1.split()
    print(f"Words : {len(var1)}")

    # Counting lines
    file.seek(0)
    var2 = file.readlines()
    print(f"Lines : {len(var2)}")

    # Counting characters
    file.seek(0)
    var3 = file.read()
    count = 0
    for i in range(len(var3)) :
        if var3[i].isalpha() :
            count += 1
    print(f"Characters : {count}")