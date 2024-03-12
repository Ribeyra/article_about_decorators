def each_pheasant(foo):
    def wrapper():
        print('каждый')
        foo()
        print('фазан')
    return wrapper


def hunter_is_sitting(foo):
    def wrapper():
        print('охотник')
        foo()
        print('сидит')
    return wrapper


def wishes_where(foo):
    def wrapper():
        print('желает')
        foo()
        print('где')
    return wrapper


def know():
    print('знать')


know = each_pheasant(hunter_is_sitting(wishes_where(know)))
know()

# каждый
# охотник
# желает
# знать
# где
# сидит
# фазан
