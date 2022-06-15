"""
Problem:
    Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

    Return true if there is a 132 pattern in nums, otherwise, return false.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: There is no 132 pattern in the sequence.
    
    Example 2:
    Input: nums = [3,1,4,2]
    Output: true
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
    
    Example 3:
    Input: nums = [-1,3,2,0]
    Output: true
    Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Solution:
    To solve this problem, we will use monotonic stack because we are trying to preserve the order by which i and j appear in the array. At any given k, j should be the maximum number to the left of k and i should be the minimum number to the left of j. Thus, we will remove all previous j that are less than or equal to k from the stack. Then, we test if i < k < j with the value on top of the stack. If the condition isn't satisfy, we add the current k as j and the minimum of k and previous minimum as i into the stack.  

    Self observation:
    1. If we don't use monotonic stack and set i to always be the minimum and j to always be the maximum, then the order of i and j will not be peserved. Test case [1,0,1,-4,-3]. 
    2. If we set it such that i only changes when j changed, i will not store the true to the left of current k. Test case [3,1,4,2]. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:

        # Monotonic decreasing stack [k, min on the left of k] or [j, i]
        mono_stack = []

        # The minimum on the left of k
        left_min = nums[0]

        for k in nums[1:]:

            # Pop all j that is less than or equal k since j < k
            while mono_stack and mono_stack[-1][0] <= k:
                mono_stack.pop()

            # Check if i < k and k < j
            if mono_stack and mono_stack[-1][1] < k and k < mono_stack[-1][0]:
                return True

            # Add a new turn k into new j and add it to the stack
            mono_stack.append([k, left_min])

            # Find the new minimum on the left of the next k.
            left_min = min(k, left_min)

        return False
