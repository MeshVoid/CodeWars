# 8 kyu level kata challenge on codewars.com

# Return Negative
# In this simple assignment you are given a number and have to make it negative. 
# But maybe the number is already negative?


def make_negative( number ):
    if number >=0: return number * -1 
    else: return number


# shortest solution from code wars:
def make_negative( number ):
    return -abs(number)