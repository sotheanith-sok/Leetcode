"""
Problem:
    You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

    Return true if and only if we can do this so that the resulting number is a power of two.

    Example 1:
    Input: n = 1
    Output: true
    
    Example 2:
    Input: n = 10
    Output: false

Solution:
    To generate every combinations of n and check if each combination is a power of 2 would require O(m!) running time where m is the length of n. 
    
    A better approach is count digits in n and check if the count is equal to the count of a number that we know to be the power of 2. This approach will reduce the running time to O(31m) because 2**30 is larger than the largest n which is 10**9. 

Complexity:
    Time: O(m)
    Space: O(m)
"""


from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        # Count all digits in n
        n = Counter(str(n))

        # Find counts of all power of 2 from 2**0 to 2**30
        for i in range(0, 31):

            # If the current count is equal to the count of n
            if Counter(str(2 ** i)) == n:

                # Return True
                return True

        # Else, return False
        return False

