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


@wishes_where
@hunter_is_sitting
@each_pheasant
def know():
    print('знать')


know()

# желает
# охотник
# каждый
# знать
# фазан
# сидит
# где
