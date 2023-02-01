def find_gcd(a, b) :
    if a == 0 :
        return b
    
    return find_gcd(b % a, a)

p = int(input('Enter first number : '))
q = int(input('Enter second number : '))

res = find_gcd(p, q)

print(f"GCD of {p} and {q} is : {res}")