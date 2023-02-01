import random
import time

random.seed(time.time())

def coin() :
    n = random.choice(['head', 'tails'])
    return n

def die(n) :
    res = random.randint(1, n)
    return res

print(f"Result of coin toss is : {coin()}")

n = int(input("Enter the number of sides of die : "))
res = die(n)
print(f"Throw of die is : {res}")