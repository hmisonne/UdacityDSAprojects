def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == None:
        return -1
    first_index = 0
    last_index = len(input_list) -1

    while last_index >= first_index:
        mid = (first_index + last_index) // 2
        if input_list[mid] == number:
            return mid
        elif number < input_list[mid]:
            if input_list[first_index] > number:
                first_index = mid + 1
            else:
                last_index = mid - 1
        else:
            if input_list[last_index] < number:
                last_index = mid - 1
            else:
                first_index = mid + 1
    return -1



def linear_search(input_list, number):
    if input_list == None:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print("Input List: {}".format(input_list))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass: number {} located on index: {}".format(number, linear_search(input_list, number)))
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #Expected Output: Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #Expected Output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #Expected Output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #Expected Output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #Expected Output: Pass
test_function([[], None]) #Expected Output: Pass
test_function([None, None]) #Expected Output: Pass