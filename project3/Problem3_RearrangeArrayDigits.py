def rearrange_digits(input_list):
    if input_list == None:
        return None
    return mergesort(input_list, len(input_list))

def mergesort(items, original_size):
    
    if len(items) <=1 :
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left = mergesort(left, original_size)
    right = mergesort(right, original_size)
    
    if len(left) == original_size // 2:
        return final_merge(left, right)
    else:
        return merge(left, right)

def merge(left, right):
    
    right_index = 0
    left_index = 0
    merged_list = []
    
    while right_index < len(right) and left_index < len(left):
        if left[left_index] > right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1
    merged_list += left[left_index:]
    merged_list += right[right_index:]
    return merged_list


def final_merge(left, right):
    
    right_index = 0
    left_index = 0
    
    first_number = ''
    first_digit = 0
    second_number = ''
    second_digit = 0
    
    while right_index < len(right) and left_index < len(left):
        if left[left_index] > right[right_index]:
            if first_digit <= second_digit:
                first_number += str(left[left_index])
                first_digit += 1
            else:
                second_number += str(left[left_index])
                second_digit += 1
            left_index += 1
        else:
            if first_digit <= second_digit:
                first_number += str(right[right_index])
                first_digit += 1
            else:
                second_number += str(right[right_index])
                second_digit += 1
            right_index += 1
    remaining_numbers = left[left_index:] + right[right_index:]
    for element in remaining_numbers:
        if first_digit <= second_digit:
            first_number += str(element)
            first_digit += 1
        else:
            second_number += str(element)
            second_digit += 1
    return [int(first_number), int(second_number)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print("Rearranging array: {}".format(test_case[0]))
    if output == None:
        print("Pass: None input return None output")
    elif len(output) <= 1 :
        print("Pass: Array of 1 or 0 element: {} returns same element: {}".format(test_case[0],output))
    elif sum(output) == sum(solution):
        print("Pass: Largest number are {} and {}".format(output[0],output[1]))
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[7,0,6,2,5,5], [750, 652]])
test_function([[4], [4]])
test_function([[], []])
test_function([None, None])