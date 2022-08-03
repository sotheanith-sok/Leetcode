"""
Problem:
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

    Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
    Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0

Solution:
    This solution is a modification of kth sum solution.

    Start by sorting nums. Then, recursively pick a number until you picked k-2 numbers and only if the result isn't equal to the target yet. To avoid duplication, you can only pick from subsequent numbers after the previously picked number. 

    We will use the two pointers technique to picks the last two numbers. Initialize the left pointers to the index of the last picked number adding 1 and the right pointers to the end of nums. 
    If the sum of all values including at both pointers are less than the target, increment the left pointer by 1. Else, if the sum of all values including at both pointers are greater than the taget, decrement the right pointer by 1. Else, we have found the cloest sum to the target and thus, we return. 

Complexity:
    Time: O(n**k)
    Space: O(1)
"""

from math import inf


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        # Initialize the result
        res = inf

        # Sort nums so it is easier to avoid duplication
        nums = sorted(nums)

        # k-sum backtracking
        def kSumClosest(k=3, start=0, partialTotal=0):
            nonlocal res

            # While k hasn't reach 2
            if k != 2:

                # Pick a number from nums starting from the index of the previously picked number plus 1
                for i in range(start, len(nums)):

                    # If result is equal to target, we can stop the search
                    if res == target:
                        return

                    # To avoid duplication, we skip any number that is the same as the previous number
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # Pick a number recursively
                    kSumClosest(k - 1, i + 1, partialTotal + nums[i])

                return

            # Once we have picked k - 2 numbers
            # Initialize the left and right pointers
            l, r = start, len(nums) - 1

            # Iterate until both pointers crossed
            while l < r:

                # Add all values including at both pointers together
                total = partialTotal + nums[l] + nums[r]

                # The current sum is closer to the target than the previous sum, save it
                res = total if abs(target - total) < abs(target - res) else res

                # If the current sum is greater than the target, decrement the right pointer
                if total > target:
                    r -= 1

                # If the current sum is lesser than the target, increment the left pointer
                elif total < target:
                    l += 1

                # Else, we have the cloest possible sum
                else:
                    return

        kSumClosest()

        return res
