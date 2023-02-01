
f1 = open('a.txt', 'r', encoding='utf-8')
f2 = open('b.txt', 'w', encoding='utf-8')

while True :
    char = f1.read(1)
    if not char :
        break
    if char == " " :
        continue

    f2.write(char)

f1.close()
f2.close()