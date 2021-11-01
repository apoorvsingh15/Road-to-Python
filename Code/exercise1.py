# Write a function which multiplies a given number by ten

def multiplyByTen(number):
    print(number * 10)
    return number * 10


multiplyByTen(6)

# Write a function which returns True if both of its arguments are non-zero, and False otherwise.


def checkNonZero(args1, args2):
    if args1 > 0 and args2 > 0:
        print(True)
        return True
    else:
        print(False)
        return False


checkNonZero(1, 2)
checkNonZero(0, 2)
