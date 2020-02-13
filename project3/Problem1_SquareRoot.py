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

print ("Pass" if  (3 == sqrt(9)) else "Fail") # Expected: Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Expected: Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # Expected: Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") # Expected: Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # Expected: Pass
print ("Pass" if  (5 == sqrt(30)) else "Fail") # Expected: Pass