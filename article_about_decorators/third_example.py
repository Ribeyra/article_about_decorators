def memoize(amount):
    args_list = []
    memoize_dict = {}

    def inner(foo):
        def wrapper(arg):
            if arg not in memoize_dict:
                if len(args_list) == amount:
                    value = args_list.pop(0)
                    memoize_dict.pop(value)
                args_list.append(arg)
                new_value = foo(arg)
                memoize_dict[arg] = new_value
            return memoize_dict[arg]
        return wrapper
    return inner


@memoize(3)
def long_running_foo(arg):
    """ some text """
    print('processing..', end=' ')
    return arg


print(long_running_foo(1))      # processing.. 1
print(long_running_foo(2))      # processing.. 2
print(long_running_foo(3))      # processing.. 3
print(long_running_foo(2))      # 2
print(long_running_foo(3))      # 3
print(long_running_foo(4))      # processing.. 4
print(long_running_foo(3))      # 3
print(long_running_foo(1))      # processing.. 1
