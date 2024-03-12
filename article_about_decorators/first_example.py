def decorator(foo):
    def wrapper():
        print('text before foo call')
        foo()
        print('text after foo call')
    return wrapper


def greet():
    print('Hello')


greet()    # => Hello

greet = decorator(greet)    # Декорируем функцию

greet()     # => text before foo call
            # => Hello
            # => text after foo call
