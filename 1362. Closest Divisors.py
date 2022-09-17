"""
Problem:
    Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

    Return the two integers in any order.

    Example 1:
    Input: num = 8
    Output: [3,3]
    Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
    
    Example 2:
    Input: num = 123
    Output: [5,25]
    
    Example 3:
    Input: num = 999
    Output: [40,25]

Solution:
    If two numbers multiply to num, their range must be between 0 < num1, num2 <= num. However, we don't have to search through the entire range because the distance between num1 and num2 will decreasing until num1==sqrt(num) and then, it will increase instead. Thus, start from num1 = sqrt(num),...,1, we will calculate num2 and return the first occurence of num1 and num2 where both are integers. 

Complexity:
    Time: O(sqrt(num))
    Space: O(1)
"""

from math import sqrt


class Solution:
    def closestDivisors(self, num: int) -> list[int]:

        # Use num + 2 as the upper bound and start searching from sqrt(num + 2),...,1
        for i in range(int(sqrt(num + 2)), 0, -1):

            # Check if num1 and num2 are integers and multiply up to num + 1 or num + 2
            for j in range(1, 3):

                # If num2 isn't an integer, continue
                if (num + j) % i != 0:
                    continue

                # Else, we have found the solution
                return [i, (num + j) // i]

