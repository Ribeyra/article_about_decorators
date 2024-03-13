from functools import wraps


def each_pheasant(foo):
    @wraps(foo)
    def wrapper():
        print('каждый')
        foo()
        print('фазан')
    return wrapper


def hunter_is_sitting(foo):
    @wraps(foo)
    def wrapper():
        print('охотник')
        foo()
        print('сидит')
    return wrapper


def wishes_where(foo):
    @wraps(foo)
    def wrapper():
        print('желает')
        foo()
        print('где')
    return wrapper


def know():
    print('знать')


original_know = know    # получаем еще одну переменную
print(know)             # <function know at 0x7fa16ccab130>
know = each_pheasant(hunter_is_sitting(wishes_where(know)))
print(know)             # <function know at 0x7fa16ccab2e0>
function_without_first_wrapper = know.__wrapped__
function_without_second_wrapper = function_without_first_wrapper.__wrapped__
function_without_third_wrapper = function_without_second_wrapper.__wrapped__
print(function_without_third_wrapper is original_know)     # True


# print(long_running_foo.__dict__)
# x = long_running_foo.__wrapped__
# print(x.__dict__)
