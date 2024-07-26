'''
You are given a list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the min number of times the original sorted list was rotated to obtain the given list.
Function should have O(logN) complexity, where N = length of list. Assume all numbers in list are unique.

Eg.
Output = [5, 6, 9, 0, 2, 3, 4]
Num rotations = 3
Input = [0, 2, 3, 4, 5, 6, 9]

Rotating list =
pop last element and add it before first element.
i.e. [3, 2, 4, 1] => [1, 3, 2, 4] after 1 rotation.

'''

# Brute-Force Solution
'''
Check for each number and its predecessor. If the number is smaller than its predecessor, that number's position is the amount of times
the list was rotated.


'''

