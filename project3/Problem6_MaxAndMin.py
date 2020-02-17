def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None or len(ints) == 0:
        return None
    if len(ints) == 1:
        min_number = ints[0]
        max_number = ints[0]
    else:
        if ints[0] < ints[1]:
            min_number = ints[0]
            max_number = ints[1]
        else:
            min_number = ints[1]
            max_number = ints[0]
    for number in ints[2:]:
        if number < min_number:
            min_number = number
        elif number > max_number:
            max_number = number
    return (min_number, max_number)

## Example Test Case of Ten Integers
import random


def test_random(l):
    print('Test for array: {}'.format(l))
    print ("Pass: tuple found: {}".format(get_min_max(l)) if ((0, 9) == get_min_max(l)) else "Fail")
def test(l):
    print('Test for array: {}'.format(l))
    if get_min_max(l) == None:
        print('Incorrect value')
    else:
        print ("Pass: tuple found: {}".format(get_min_max(l)) if (min(l) == get_min_max(l)[0] and max(l) ==get_min_max(l)[1] ) else "Fail")
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
test_random(l)
random.shuffle(l)
test_random(l)
test([5,4,2])
test([5])
test([])
test(None)