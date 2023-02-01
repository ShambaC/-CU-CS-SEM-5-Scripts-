# using while loops do gausian addition on a list having even number of numbers. Print each partial sum
# Eg : If the list is [1,2,3,4,5,6] the program should give the following output : 
# "1+6", "2+5" and "3+4" in seperate lines.
# Extend it to handle a odd length

l = [1,2,3,4,5,6]
i = sum = 0
j = len(l)
print(f"Given list is : {l}")
k = j - 1

print("Sum of all the elements from the above list using gaussian addition : ")
while i < k :
    print(f"After sum {i + 1} : {l[i]} + {l[k]} = {l[i] + l[k]}")
    sum = sum + l[i] + l[k]
    i = i + 1
    k = k - 1

print(f"Sum : {sum}")