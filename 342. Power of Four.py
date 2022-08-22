"""
Problem:
    Given an integer n, return true if it is a power of four. Otherwise, return false.

    An integer n is a power of four, if there exists an integer x such that n == 4x.

    Example 1:
    Input: n = 16
    Output: true
    
    Example 2:
    Input: n = 5
    Output: false
    
    Example 3:
    Input: n = 1
    Output: true

Solution:
    In theroy, using log(n,4) would work but it isn't in practice due to floating point numbers inaccuracy. ie. 1.99999 could be an indication of n not being a power of 4 or just a floating point inaccuracy. Thus, we will use a bit minipulation instead. 

    There are 3 criteria that n need to be meet to be a power of 4.
        1. n must be bigger than 0
            n > 0

        2. n must be a power of 2
            n & (n-1) == 0
            We want to filter out n that is a non-power of 2 that could meet the next filter criteria such as 20
            
        3. n must be a power of 4
            n & 1431655765 == n

            1431655765 == b'1010101010101010101010101010101 or xor of 
            0:                                        1
            4:                                      100
            16:                                   10000
            64:                                 1000000
            256:                              100000000
            1024:                           10000000000
            4096:                         1000000000000
            16384:                      100000000000000
            65536:                    10000000000000000
            262144:                 1000000000000000000
            1048576:              100000000000000000000
            4194304             10000000000000000000000
            16777216:         1000000000000000000000000
            67108864:       100000000000000000000000000
            268435456:    10000000000000000000000000000
            1073741824: 1000000000000000000000000000000
                        1010101010101010101010101010101


    Ex: Given n = [-4, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Step 1: n > 0
        n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    Step 2: n & (n-1) == 0
        n = [2, 4, 8]

    Step 3: n & 1431655765 == n
        n = [4]

Complexity:
    Time: O(1)
    Space: O(1)
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # Check if n meets the three criteria
        return n > 0 and n & (n - 1) == 0 and n & 1431655765 == n

