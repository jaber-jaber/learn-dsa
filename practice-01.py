'''
Linear Search Algorithm

In this algorithm, we are given a list of numbers and a query. We're supposed to find the query number in the list, and return its position.
Eg.

input = [1, 2, 3, 4, 5]
query = 3
output = 2

'''

def locate_number(numbers, query):
    # Var position with value 0
    position = 0

    while position < len(numbers):
        if numbers[position] == query:
            return position
        position += 1
    return -1


'''
Binary Search

In BS, we check the middle number first. Then because the list is sorted (if not sorted, then sort first) we check the side where the number is less than or greater than
the numbers on the respective side.


input = [1, 2, 3, 4, 5]
query = 5
We check 3 first, then because its sorted and we want 5, we check the two after 3. Specifically, we pick the 4 here (always go for middle).

We can define a helper function here to cover the edge case where multiple cases of the query are in the list. I.e.
input = [8, 6, 6, 6, 6, 6, 5, 4, 3, 3, 8]
query = 6

It should return 1, but because we're starting in the middle with BS, it will actually return
output = 5

Runs 55,000 faster than linear search.

'''

def locate_number(numbers, query):
    lo, hi = 0, len(numbers) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(numbers, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1

    return -1 

def test_location(numbers, query, mid):
    mid_number = numbers[mid]
    
    if mid_number == query:
        if mid-1 >= 0 and numbers[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    

