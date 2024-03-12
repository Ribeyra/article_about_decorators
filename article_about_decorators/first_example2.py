def decorator(foo):
    def wrapper():
        print('text before foo call')
        foo()
        print('text after foo call')
    return wrapper


@decorator
def greet():
    print('Hello')


greet()     # => text before foo call
            # => Hello
            # => text after foo call
