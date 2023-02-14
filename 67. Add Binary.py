"""
Problem:
    Given two binary strings a and b, return their sum as a binary string.
    
    Example 1:
    Input: a = "11", b = "1"
    Output: "100"
    
    Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Solution:
    We will add both numbers together one bit at a time. Iterate until a, b, and carry bit are 0. At each iteration, sum the least significant bits of a and b with carry bit. The carry bit will 1 if the sum is greater than 1 else it is 0. The result bit will be 1 if the sum if odd else it will be 0. Shift a and b to the right by 1 bit and continue to the next iteration.  

Complexity:
    Time: O(n) where n is the largest number of bits between a and b
    Space: O(n)
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Convert a and b to int for easier bit minipulation and initialize the carry bit
        a, b, carry = int(a, 2), int(b, 2), 0

        # Initialize the result
        res = []

        # Iterate until a, b, and the carry bit are 0
        while a or b or carry:

            # Sum the least significant bits of a and b with carry bit
            bitSum = (a & 1) + (b & 1) + carry

            # The next carry bit will 1 if the sum is greater than 1 else it is 0
            carry = 1 if bitSum > 1 else 0

            # The result bit will be 1 if the sum if odd else it will be 0
            res.append(str(int(bitSum % 2 != 0)))

            # Shift both a and b by 1 bit to the right
            a, b = a >> 1, b >> 1

        return "".join(res[::-1]) if res else "0"
