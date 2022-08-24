"""
Problem:
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.

    
    Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]
    
    Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]
    
    Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]

Solution:
    To find the next permutation, we want to increase the sequence as little as possible. Start from the end of the list and find a number that is less than its next number and use such number as the pivot. 
    We know that the sequence at the right of the pivot is strictly non-decreasing. 
    
    Then, we want to swap the number at the pivot with a number at its right sequence that is larger but cloest to the pivot. This will increase the value at the pivot while maintaining the non-decreasing nature of the right sequence. 
    
    Finally, reverse the right sequence to reduce it the minimum because a reversal of non-decreasing sequence will result in the minimum of such sequence.  


Complexity:
    Time: O(n)
    Space: O(1)
"""


from math import inf


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Get the length of nums
        n = len(nums)

        # 1. Find the pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # 2. If there is a pivot
        if pivot >= 0:

            # Find the larger value at the right sequence that is cloest to the pivot
            nextToPivot = None

            # Start searching from the right
            for i in range(n - 1, pivot, -1):
                if nums[pivot] < nums[i] < (nums[nextToPivot] if nextToPivot else inf):
                    nextToPivot = i

            # Swap the two values
            nums[pivot], nums[nextToPivot] = nums[nextToPivot], nums[pivot]

        # 3. Reverse the right sequence
        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])


