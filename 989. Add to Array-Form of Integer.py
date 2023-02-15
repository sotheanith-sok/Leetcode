"""
Problem:
    The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

    Example 1:

    Input: num = [1,2,0,0], k = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234
    
    Example 2:
    Input: num = [2,7,4], k = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455
    
    Example 3:
    Input: num = [2,1,5], k = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

Solution:
    Let k be the carry and continue to add all digits of num with the carry. At each iteration, pop the least significant digits of num and carry and add them together. Store the least significant digit of the partial sum into the result and the remaining digits back into the carry.   

Complexity:
    Time: O(n) where n is the maximum length between num and k
    Space: O(n)
"""


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        # Initialize the result and the carry
        res, carry = [], k

        # Iterate until we added all digits of num and carry
        while carry or num:

            # Add the least significant digits of num and carry together
            pSum = (num.pop() if num else 0) + (carry % 10)

            # Store the least significant digit of the partial sum into the result
            res.append(pSum % 10)

            # Add the remaining digits back into the carry
            carry = carry // 10 + pSum // 10

        return res[::-1]
