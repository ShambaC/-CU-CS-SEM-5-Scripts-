s = input("Enter a sentence : ")

s_string = s.split()
s1 = " ".join(s_string[1::2])
s2 = " ".join(s_string[0::2])

print(f"Odd words : {s1}")
print(f"Even words : {s2}")