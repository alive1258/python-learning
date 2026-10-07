from math import *
from random import *
result = ceil(3.7)
print(result)
result = floor(3.7)
print(result)
result = randint(1, 10)
print(result)
print("Random float between 0 and 1:", random())
print("Random float between 1 and 10:", uniform(1, 10))
print("Random choice from list:", choice([1, 2, 3, 4, 5]))
print("Random sample of 3 from list:", sample([1, 2, 3, 4, 5], 3))
print("Random shuffle of list:", end=" ")
my_list = [1, 2, 3, 4, 5]
