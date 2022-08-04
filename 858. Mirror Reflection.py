"""
Problem:
    There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

    The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

    Given the two integers p and q, return the number of the receptor that the ray meets first.

    The test cases are guaranteed so that the ray will meet a receptor eventually.

    Example 1:
    Input: p = 2, q = 1
    Output: 2
    Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
    
    Example 2:
    Input: p = 3, q = 1
    Output: 1

Solution:
    Determine how many times we have to flip the the mirror horizontally and vertically until we reach a corner aka how many time do we have to multiply q by until it reaches a multiple of p. Let n be the multiple of q aka horizontal flip and m be the multiple of p aka vertical flip. 
    If n is odd and m is even, it will reach 0. 
    If n is odd and m is odd, it will reach 1.
    If n is even and m is odd, it will reach 2 

Complexity:
    Time: O(q//p)
    Space: O(1)
"""


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:

        n = 1

        # Find how the muliple of q until n*q is a multiple of p
        while (n * q) % p != 0:
            n += 1

        # If n is odd and m is even, it will reach 0
        if n % 2 == 1 and (n * q // p) % 2 == 0:
            return 0

        # If n is odd and m is odd, it will reach 1
        if n % 2 == 1 and (n * q // p) % 2 == 1:
            return 1

        # If n is even and m is odd, it will reach 2
        if n % 2 == 0 and (n * q // p) % 2 == 1:
            return 2

