""" 
Problem:
    A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

    For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
    In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
    A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

    Given an integer array nums, return the length of the longest wiggle subsequence of nums.

    Example 1:
    Input: nums = [1,7,4,9,2,5]
    Output: 6
    Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
    
    Example 2:
    Input: nums = [1,17,5,10,13,15,10,5,16,8]
    Output: 7
    Explanation: There are several subsequences that achieve this length.
    One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
    
    Example 3:
    Input: nums = [1,2,3,4,5,6,7,8,9]
    Output: 2

Solution:
    We will use two varaibles to keep track of the longest subsequent that ended with a positive different and a negative different. Initially, both varaibles will be 1. Then, we will iterate through all nums and check each pair. If the current num is larger than the previous num, we will increment the negative difference by 1 and save it as the new positive difference. If the current num is smaller than the previous num, we will increment the positive difference by 1 and save it as the new negative difference. 

Complexity:
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:

        # If the length of nums is less than 2, we will return the len of nums as our base case
        if len(nums) < 2:
            return len(nums)

        # Initialize the length of the positive and the negative ended subsequent
        pos, neg = 1, 1

        for i in range(1, len(nums)):

            # If the current num is larger than the previous num,
            if nums[i] > nums[i - 1]:

                # Increment the positive ended subsequent
                pos = neg + 1

            # Else if the current num is less than the previous num,
            elif nums[i] < nums[i - 1]:

                # Increment the negative ended subsequent
                neg = pos + 1

        # Return the longest subsequent
        return max(pos, neg)

