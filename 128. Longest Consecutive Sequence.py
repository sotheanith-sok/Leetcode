""" 
Problem:
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    
    Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Solution:
    Convert nums from a list to a set to eliminate duplication. Then, initialize a set to keep track of any number that has been used to form a previous subsequence. Iterate through all numbers that haven't been used. Starting from the current number, mark it as used and initialize the length of the subsequence as 1. Then, check if there exists other numbers 1 less than or larger than the current number. If yes, update the length and mark those numbers as used too. Continue until the condition is no longer true. Finally, save the length if it is larger than previous length. Continue to the next unsued number.  

Complexity:
    Time: O(n) where n is the number of unique numbers in nums
    Space: O(n) where n is the number of unique numbers in nums

"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # Convert nums to a set and initialize a set to keep track of used number
        nums, used = set(nums), set()

        # Initialize the result
        res = 0

        # Iterate through all numbers
        for n in nums:

            # If it is used, skip to the next number
            if n in used:
                continue

            # Else, intialize the length of this subsequence as 1
            length = 1

            # Initialize the left and right pointers
            l = r = n

            # While there exists a number 1 less than the left pointer,
            while l - 1 in nums:

                # Increment the length by 1
                length += 1

                # Mark it as used
                used.add(l - 1)

                # Decrement the left pointer
                l -= 1

            # While there exists a number 1 larger than the right pointer,
            while r + 1 in nums:

                # Increment the length by 1
                length += 1

                # Mark it as used
                used.add(r + 1)

                # Increment the right pointer
                r += 1

            # Update the result
            res = max(res, length)

        return res

