"""
Problem:
    Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

    Example 1:
    Input: n = 1
    Output: 1
    Explanation: "1" in binary corresponds to the decimal value 1. 
    
    Example 2:
    Input: n = 3
    Output: 27
    Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
    After concatenating them, we have "11011", which corresponds to the decimal value 27.
    
    Example 3:
    Input: n = 12
    Output: 505379714
    Explanation: The concatenation results in "1101110010111011110001001101010111100".
    The decimal value of that is 118505380540.
    After modulo 10**9 + 7, the result is 505379714.

Solution:
    Initialize the result to 0. Then, iterate 0 to n + 1. At each iteration, shift res by bit length of the current number and xor the shifted res with the current number. Lastly, return the result modded by 10**9+7

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:

        # Intialize the result
        res = 0

        # Iterate through all numbers from 0 to n
        for i in range(n + 1):

            # Shift result by bit length of the current number and xor the shifted result with the current number
            res = ((res << i.bit_length()) ^ i) % (10 ** 9 + 7)

        return res

