import math

def round_float_if_close(number, delta):
    lower = math.floor(number)
    upper = math.ceil(number)



    diff_to_lower = abs(number - lower)
    diff_to_uppper = abs(number - upper)



    if diff_to_lower <= delta:
        result = lower 
    elif diff_to_uppper <= delta:
        result = upper

    else:
        result = number 

    return int(result)