""" 
Problem:
    A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

    Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

    Example 1:
    Input: n = "32"
    Output: 3
    Explanation: 10 + 11 + 11 = 32
    
    Example 2:
    Input: n = "82734"
    Output: 8
    
    Example 3:
    Input: n = "27346209830709182346"
    Output: 9

Solution:
    The most we can take away from each digit is 1 and we dont want to subtract from a digit that is 0. Thus, the minimum steps requires to reduce the entire number to 0 is the same as the minimum steps requirs to reduce largest digit to 0.  

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)
