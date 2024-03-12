def decorator(foo):
    def wrapper(*args):
        foo(*args)
    wrapper.__name__ = foo.__name__
    wrapper.__doc__ = foo.__doc__
    return wrapper


@decorator
def print_greet(name):
    """Some description"""
    print('Hello, ' + name + '!')


print(print_greet.__name__)     # print_greet
print(print_greet.__doc__)      # Some description
