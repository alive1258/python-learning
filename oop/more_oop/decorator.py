def my_decorator(func):
    def wrapper():
        print("Before function execution")

        func()

        print("After function execution")

    return wrapper
 

@my_decorator
def say_hello():
    print("Hello, Python!")


say_hello()
