# 8 kuy level challenge from codewars.com
# Given a set of numbers, return the additive inverse of each. 
# Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []


def invert(lst):
    result = []
    for i in lst: 
        i = i * -1
        result.append(i)
    return result

print(invert([1,2,3,4,5]))

# best solution from code wars, one-liner way better than mine:

def invert(lst):
    return [-x for x in lst]