""" 
Problem:
    Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

    In one move, you can increment or decrement an element of the array by 1.

    Test cases are designed so that the answer will fit in a 32-bit integer.

    Example 1:
    Input: nums = [1,2,3]
    Output: 2
    Explanation:
    Only two moves are needed (remember each move increments or decrements one element):
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
    
    Example 2:
    Input: nums = [1,10,2,9]
    Output: 16

Solution:
    For any given array, the closest element to all elements in such array is the median. Thus, we can either sort the array and find the median (O(nlogn)) or use a quick selection to find the median (avg: O(n), worst case O(n**2)). Then, we simply total the difference between each element and median to find the solution. Noted that if we can partition the array into two similarly sized subarray, we can simplify the problem further and exclude the need to find the median.
    
    ie: array = [a,b,c,d,e] median = c
        total = c-a + c-b + c-c + d-c + e-c
              = - a - b + d + e
              = e-a + d-b

Complexity:
    Time: O(nlogn)
    Space: O(1)

"""


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Sort nums such that we can partition into two parts.
        # Left partition will be smaller than median
        # Right partition will be larger than median
        nums.sort()

        # Initialize the result, the left pointer and the right pointer.
        res = 0
        l, r = 0, len(nums) - 1

        # Iterate until the left and the right pointer cross
        while l < r:

            # Add the number at the right pointer to and subtract the number at the left pointer from the result
            res += nums[r] - nums[l]

            # Update pointers
            l, r = l + 1, r - 1

        return res

