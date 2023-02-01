import random
import time

random.seed(time.time())

def coin() :
    sides = ['head', 'tails']
    weight = [9, 1]
    n = random.choices(sides, weights=weight)
    return n

def die() :
    sides = [1, 2, 3, 4, 5, 6]
    weight = [5, 12, 4, 3, 22, 1]
    res = random.choices(sides, weights=weight)
    return res

print(f"Result of coin toss is : {coin()}")

print(f"Side of die : {die()}")