"""
Problem:
    You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.

    Example 1:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2
    
    Example 2:
    Input: nums = [3,3,7,7,10,11,11]
    Output: 10

Solution:
    Perform a binary search on the given list of numbers to find the target. When we split the list into two partitions, we have to ensure that any duplicate numbers ended up in the same partition. Then, we will only have to search any sub partition that has an odd length.

Complexity:
    Time: O(log n)
    Space: O(1)
"""


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:

        # Find the length of nums
        n = len(nums)

        # Initialize the left and right pointers
        l, r = 0, n - 1

        # Iterate until the left and right pointers crossed
        while l <= r:

            # Calcualate the mid pointer
            m = (r - l) // 2 + l

            # Shift the mid pointer such that it points to the first occurence of any numbers
            m -= (0 <= m - 1 < n) and nums[m - 1] == nums[m]

            # If there is only a single number left in the partition or there doesn't exist a duplicate number next to the current number,  we have found the result
            if l == r or ((not (0 <= m + 1 < n) or nums[m + 1] != nums[m])):
                return nums[m]

            # Else, if the left partition has odd length, search it
            if (m - l) % 2 != 0:
                r = m - 1

            # Else, search the right partition
            else:
                l = m + 2
