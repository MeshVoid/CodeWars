# 8th kyu challenge task from codewars.com

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

# Solution:
def square_sum(numbers):
    square_sum = 0
    for i in numbers: square_sum += int(i)**2
    return square_sum