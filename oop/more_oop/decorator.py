def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")

        result = func(*args, **kwargs)

        print("After function execution")
        return result

    return wrapper


@my_decorator
def say_hello():
    print("Hello, Python!")


@my_decorator
def get_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    return factorial


say_hello()

result = get_factorial(5)
print("Factorial:", result)