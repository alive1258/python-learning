# Example 1: Inner Function
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    # Calling the inner function
    inner_function()


outer_function()


# Example 2: Inner Function with Return Value
def calculate():
    def add(a, b):
        return a + b

    result = add(10, 20)
    return result


print("Sum:", calculate())


# Example 3: Wrapper Function
def wrapper_function():
    def inner_function():
        print("Inner function is running")

    print("Before calling inner function")
    inner_function()
    print("After calling inner function")


wrapper_function()
