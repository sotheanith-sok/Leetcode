"""
Problem:
    A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

    You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

    Return the minimum number of flips to make s monotone increasing.

    Example 1:
    Input: s = "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.
    
    Example 2:
    Input: s = "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.
    
    Example 3:
    Input: s = "00011000"
    Output: 2
    Explanation: We flip to get 00000000.

Solution:
    We need to find a place to divide a string into two partitions where the left parition contains only 0s and the right partiion only contains 1s. Maintain two variables to keep track of the number of 0s and 1s for each partition. Then, iterate through all characters in the given. At each character, transfer the current character from the right into the left partition and calculate the number of swap required to create a monotinocally increasing string.  

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        # Find the length of the string
        n = len(s)

        # Initialize the two partitions where the right partition contains all characters
        left, right = 0, s.count("1")

        # If the right partition contains all 0s or 1s, return 0
        if right == 0 or right == n:
            return 0

        # Else, initialize the result
        res = min(right, n - right)

        # Iterate through all characters
        for i, c in enumerate(s, 1):

            # Transfer the current character from the right into the left partition
            left, right = left + int(c == "0"), right - int(c == "1")

            # Calculate the number of swap required to create a monotinocally increasing string
            res = min(res, i - left + n - i - right)

        return res
