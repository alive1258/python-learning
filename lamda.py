#lamda
def double(x):
    return x * 2
result = double(5)
print(result)  # Output: 10

duble_lambda = lambda num: num * 2
result = duble_lambda(5)
print(result)  # Output: 10


add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

actor=[
    {"name":"John","age":30},
    {"name":"Alice","age":25},
    {"name":"Bob","age":35},
    {"name":"Charlie","age":28}

    ]

junior=list(filter(lambda actor: actor["age"] < 30, actor))