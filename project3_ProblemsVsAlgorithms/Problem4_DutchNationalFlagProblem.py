def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None:
        return None
    index_next0 = 0
    index_next2 = len(input_list)-1
    index = 0
    while index <= index_next2:
        element = input_list[index]
        if element == 0:
            input_list[index] = input_list[index_next0]
            input_list[index_next0] = 0
            index_next0 += 1
            index += 1

        elif element == 2:
            input_list[index] = input_list[index_next2]
            input_list[index_next2] = 2
            index_next2 -= 1
        else:
            index += 1
        
    return input_list

def test_function(test_case):
    print('sorting the array: {}'.format(test_case))
    sorted_array = sort_012(test_case)
    if sorted_array == None:
        print('None input returns None')
    else:
        print('new array: {}'.format(sorted_array))
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0])
test_function([])
test_function(None)