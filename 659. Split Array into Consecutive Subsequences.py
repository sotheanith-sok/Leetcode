"""
Problem:
    You are given an integer array nums that is sorted in non-decreasing order.

    Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

    Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
    All subsequences have a length of 3 or more.
    Return true if you can split nums according to the above conditions, or false otherwise.

    A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

    Example 1:
    Input: nums = [1,2,3,3,4,5]
    Output: true
    Explanation: nums can be split into the following subsequences:
    [1,2,3,3,4,5] --> 1, 2, 3
    [1,2,3,3,4,5] --> 3, 4, 5
    
    Example 2:
    Input: nums = [1,2,3,3,4,4,5,5]
    Output: true
    Explanation: nums can be split into the following subsequences:
    [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
    [1,2,3,3,4,4,5,5] --> 3, 4, 5
    
    Example 3:
    Input: nums = [1,2,3,4,4,5]
    Output: false
    Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.

Solution:
    Start by counting numbers and their frequencies and store them in an ordered dict. Then, let cn be the current number and pn be the previous number. Let p1, p2, p3 be the number of sequences ended at pn and has length 1, 2, and 3+. Let c1, c2, c3 be the number of sequences ended at cn and has length 1, 2, and 3+. Initially, p1, p2, p3 = counts[first number], 0, 0.
    Itearte through the remaining numbers. 

    if cn != pn + 1:
        return False if there is any sequences of length 1 and 2 leading up to pn because we can't increase them any longer.
    Else, 
        if count[cn] < p1 + p2
            return False because there isn't enough counts of cn to to the increase all sequences of length 1 and length 2 leading up to pn. 
        Else,

            c1 = max(count - (p1 + p2 + p3), 0) # The remaining unused cn after p1, p2, and p3 bounded at 0.

            c2 = p1 # c2 = p1 because count[cn] >= p1 + p2. Thus, there will always be enough cn to increase all sequences of length 1 and 2 leading up to pn.
            
            c3 = p2 + min(p3, count - (p1 + p2)) # The same as above case but p2 instead and we also have use any left over current number to increase the length of p3. 

Complexity:
    Time: O(n)
    Space: O(1)
"""
from collections import OrderedDict


class Solution:
    def isPossible(self, nums: list[int]) -> bool:

        # Initialize an ordered dict
        counts = OrderedDict()

        # Add all numbers to the dict
        for n in nums:
            counts[n] = counts[n] + 1 if n in counts else 1

        # Get all unique numbers
        nums = list(counts.keys())

        # Initialize the number of sequences for the first number
        p1, p2, p3 = counts[nums[0]], 0, 0

        # Iterate through the remaining number
        for i in range(1, len(nums)):

            # Find the count of the current number
            count = counts[nums[i]]

            # Initialize the number of sequences leading up to the current number
            c1, c2, c3 = count, 0, 0

            # If the current isn't one more than the previous number
            if nums[i] != nums[i - 1] + 1:

                # Check if there is any remaining sequences of length 1 and 2 leading up to previous number
                if p1 != 0 or p2 != 0:

                    # If yes, return False because it is no longer possible to increase sequences ended at the previous number
                    return False

            # Else, if the current number is one more than the previous number
            else:

                # If the count of the current number is less than the number of sequences of length 1 and 2 leading up to the previous number
                if count < p1 + p2:

                    # Return False because we can't increase the length of all those sequences
                    return False

                # Else, calculate the number sequences leading up the current number
                # c1 is the remaining current number that haven't been used for p1, p2, p3
                # c2 is always equal to p1 because count >= p1 + p2 and thus, there will always be enough cn to increase all sequences of length 1 and 2 leading up to pn
                # c3 is the same as above case but p2 instead and we also have use any left over current number to increase the length of p3

                c1, c2, c3 = (
                    max(count - (p1 + p2 + p3), 0),
                    p1,
                    p2 + min(p3, count - (p1 + p2)),
                )

            # Set the number of sequences of the current number as the previous number and continue to the next number
            p1, p2, p3 = c1, c2, c3

        # Once, we processed all number
        # If there isn't any remaining sequence of length 1 and 2, return True 
        # Else, return False
        return p1 == 0 and p2 == 0

