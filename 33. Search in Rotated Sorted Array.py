"""
Problem:
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Example 3:
    Input: nums = [1], target = 0
    Output: -1

Solution:
    Use binary search to solve this problem. Since we are rotating the list based on a pivot, for some arbitrary mid point, we know that one side of such point will be in an increasing order. Thus, we need to figure out which side is such an increasing order at and check if the target is between those two values. If yes, we search on that side. Else, we search on the other side. 

    Ex: nums = [4,5,6,7,0,1,2], target = 0

    l   r   list                mid     midValue       sideWithAnIncreasingOrder   targetBetweenSuchRange
    0   6   [4,5,6,7,0,1,2]     3       7              left                        no
    4   6   [0,1,2]             5       1              left                        yes
    4   4   [0]                 4       0                          

Complexity:
    Time: O(logn)
    Space: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # Find the length of nums
        n = len(nums)

        # Perform the binary search
        def binarySearch(l, r):

            # Calculate the mid pointer
            m = (r - l) // 2 + l

            # If the value at the mid pointer is equal to the target, return the mid pointer
            if nums[m] == target:
                return m

            # If the left and right pointers are in a valid range
            if 0 <= l < r < n:

                # If the left side is the increasing order side
                if nums[l] <= nums[m]:

                    # If the target is between such range
                    if nums[l] <= target < nums[m]:

                        # Search such side
                        return binarySearch(l, m - 1)

                    # Else, search the right side
                    else:
                        return binarySearch(m + 1, r)
                
                # Else, if the right side is the increasing order side
                else:

                    # If the target is between such range
                    if nums[m] < target <= nums[r]:

                        # Search such side
                        return binarySearch(m + 1, r)
                    
                    # Else, search the left side
                    else:
                        return binarySearch(l, m - 1)

            return -1

        return binarySearch(0, n - 1)

