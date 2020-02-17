def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    first = 1
    last = number
   
    while last >= first:
        mid = (last + first) // 2 
        if mid * mid == number:
            return mid
        elif mid * mid > number:
            last = mid - 1
        elif mid * mid < number:
            first = mid + 1
            result = mid
    return result

def test(number, expected_result):
    if sqrt(number) == expected_result:
        print("Pass: Square Root of {} equals to {}".format(number, expected_result))
    else:
        print("Fail: Expected Result: {} Vs: {}".format(expected_result, sqrt(number)))

test(9,3) # Pass
test(1,1) # Pass
test(27,5) # Pass
test(30,5) # Pass
test(-2,'invalid input') # Pass
test(None,'invalid input') # Pass