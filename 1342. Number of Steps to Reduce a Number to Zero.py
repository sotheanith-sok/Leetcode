"""
Problem:
    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

    Example 1:
    Input: num = 14
    Output: 6
    Explanation: 
    Step 1) 14 is even; divide by 2 and obtain 7. 
    Step 2) 7 is odd; subtract 1 and obtain 6.
    Step 3) 6 is even; divide by 2 and obtain 3. 
    Step 4) 3 is odd; subtract 1 and obtain 2. 
    Step 5) 2 is even; divide by 2 and obtain 1. 
    Step 6) 1 is odd; subtract 1 and obtain 0.
    
    Example 2:
    Input: num = 8
    Output: 4
    Explanation: 
    Step 1) 8 is even; divide by 2 and obtain 4. 
    Step 2) 4 is even; divide by 2 and obtain 2. 
    Step 3) 2 is even; divide by 2 and obtain 1. 
    Step 4) 1 is odd; subtract 1 and obtain 0.
    
    Example 3:
    Input: num = 123
    Output: 12

Solution:
    Let n be the bit length of num. In term of bitwise operation, num divide by 2 is the same as shifting num right by 1 bit. Thus, it takes n shift to reduce num to 0. A number is odd when the right most bit is 1. Thus, we can figure out how many time we have to subtract 1 from num by counting 1s bit in num. Do note that we double count when num is 1 because we can reduce num to 0 by either dividing or subtracting and so we have to subtract one from the result if num is not equal to 0. 

Complexity:
    Time: O(n) where n is the bit length of num
    Space: O(1)
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:

        # Count how many time we have divide num by 2 + how many time num is odd - 1
        return num.bit_length() + bin(num).count("1") - int(num != 0)

