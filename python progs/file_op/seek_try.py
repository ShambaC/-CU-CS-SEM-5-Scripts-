with open("d.txt", "r") as f :
    f.seek(3)
    print(f.read())