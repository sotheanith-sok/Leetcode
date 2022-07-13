"""
Problem:
    Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

    Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

    Example 1:
    Input: n = 12
    Output: 21
    
    Example 2:
    Input: n = 21
    Output: -1

Solution:
    Starting from the last digit, find a digit that is less than the previous digit. Then, swap such digit with the smallest value to the right of it that is larger than the digit. Then, sort the right side of the digit to produce the final result.  

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # Convert int to list of int
        n = list(str(n))

        # Iterate from the last digit
        for i in range(len(n) - 2, -1, -1):

            # Find a value that is less than previous value
            if n[i] < n[i + 1]:

                # Find the index of the smallest value to the right of the value that is larger than it
                j = len(n) - n[::-1].index(min([m for m in n[i + 1 :] if m > n[i]])) - 1
                
                # Swap values
                n[i], n[j] = n[j], n[i]

                # Sort the right side
                n = n[: i + 1] + sorted(n[i + 1 :])

                # Convert the list back to int
                n = int("".join(n))

                # Return -1 if the result is larger than the max of int32
                return n if n <= 2147483647 else -1

        return -1

