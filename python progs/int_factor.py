def find_factors(num) :
    factors = []
    
    for i in range(2, int((num/2) + 1)) :
        if num % i == 0 :
            factors.append(i)

    if len(factors) == 0 :
        print(f"{num} is a prime number !")
        return

    print(f"The factors of {num} are : ")
    print(factors)

    max_min = (factors[0], factors[len(factors) - 1])
    print('Min and max factors are : ')
    print(max_min)

a = int(input('Enter the number : '))
find_factors(a)