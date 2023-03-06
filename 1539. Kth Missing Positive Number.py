"""
Problem:
    Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

    Return the kth positive integer that is missing from this array.

    Example 1:
    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
    
    Example 2:
    Input: arr = [1,2,3,4], k = 2
    Output: 6
    Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Solution:
    Treat each number in the array as the upper bound and we can find how many missing positive integers to the left of such number in constant time. 

    Then, we can use binary search to find the range that contains kth missing positive integer and linear search to find exact value of such integer.

    Ex: arr = [2,3,4,7,11], k = 5
    l       r       mid     missing(l)  missing(mid)    search
    -1      5       2       0           1               right
    2       5       3       1           3               right
    3       5       4       3           6               left
    3       4       ----------------------------------> Linear search
Complexity:
    Time: O(logn)
    Space: O(1)
"""


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        # Find the count of existed positive integers
        n = len(arr)

        # Find the count of missing positive integers to left of a number based on its index in the arr
        def missingLeft(i):

            # If the current index is out of bound, return
            # 0 if i < 0
            # arr[-1] + k + 1 if i >= n because the largest missing positive number that can't be the answer is max(arr) + k + 1
            if not (0 <= i < n):
                return 0 if i < 0 else arr[-1] + k + 1 - n

            # Else, return the count of missing positive numbers to the left of the current number
            return arr[i] - (i + 1)

        # Start binary search
        # Set the left and right pointers to lower and upper bound of indices
        l, r = -1, n

        # Iterate until the left and right pointer meet
        while l < r:

            # If we found the range that contain kth missing positive number, perform a linear search to find its exact value
            if l == r - 1:

                # Find the lower and upper bound of missing positive numbers
                lower, upper = (
                    arr[l] if 0 <= l < n else 0,
                    arr[r] if 0 <= r < n else arr[-1] + k + 1,
                )

                # Return kth missing positive number
                return range(lower + 1, upper)[k - missingLeft(l) - 1]

            # Else, calcualate the mid pointer
            mid = (r - l) // 2 + l

            # If kth missing positive integer is between the left and mid pointer, search the left side
            if missingLeft(l) < k <= missingLeft(mid):
                r = mid

            # Else, it must be location to the right side
            else:
                l = mid
