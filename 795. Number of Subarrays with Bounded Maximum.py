"""
Problem:
    Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

    The test cases are generated so that the answer will fit in a 32-bit integer.

    Example 1:
    Input: nums = [2,1,4,3], left = 2, right = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
    
    Example 2:
    Input: nums = [2,9,2,5,6], left = 2, right = 8
    Output: 7

Solution:
    The goal is to find the number of substrings such that the largest element in each substring is between a range. Given previous substring are valid, there are three cases to consider for the current number. 

    1. If the current number is larger than the range, then it won't be able to contribute to any previous substring and thus, we skip it.
    
    Ex: arr = [1, 1, 2, 1]  range=[2, 3]   nextNum = 4
        contribution = 0 since 4 will not contribute to any previous substring.

    2. If the current number is in between the range, then it can contribute all previous substrings.

    Ex: arr = [1, 1, 2, 1]  range=[2, 3]   nextNum = 3
        contribution = 5 since 3 will contribute to all previous substring
        aka [1, 1, 2, 1, 3], [1, 2, 1, 3], [2, 1, 3], [1, 3], [3]

    3. If the current number is less than the range, then it can only contribute to previous substrings that are already valid. 

    Ex: arr = [1, 1, 2, 1]  range=[2, 3]   nextNum = 1
        contribution = 3 since 1 will contribute to some previous substrings.
        aka [1, 1, 2, 1, 1], [1, 2, 1, 1], [2, 1, 1]

    Thus, from examples above, we can see each number will contribute to the result if it is not greater than the range and the amount of contribution is based on the length of valid previous substring (valid). 
    ie arr = [1, 1, 2, 1, 1, 1] => valid = 3
       arr = [1, 1, 2, 1, 3, 1] => valid = 5
       arr = [1, 1, 2, 1, 4, 1] => valid = 0
    
    Use two pointers apporach to solve this problem. Initialize both pointers to 0 and the length of valid previous substring to 0. Use the right pointer to iterate through nums. If value at the right pointer falls between the range, we have found a valid previous substring with greater length. Else, if the value at the right pointer is greater than the range, we must reset the left pointer and the length of valid previous substring. Lastly, add the length of previous substring to the result.  


Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:

        # Initialize the length of nums, the left pointer, the length of valid previous substring, and result
        n, l, valid, res = len(nums), 0, 0, 0

        # Use the right pointer to iterate through all numbers
        for r in range(0, n):

            # If the current number falls between the range, update the length of valid previous substring
            if left <= nums[r] <= right:
                valid = r - l + 1

            # If the current number is greater than the range, reset the left pointer and the length of valid previous substring
            if nums[r] > right:
                l = r + 1
                valid = 0

            # Add the length of valid previous substring to the result
            res += valid

        return res
