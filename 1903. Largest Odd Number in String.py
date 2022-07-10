""" 
Problem:
    You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

    A substring is a contiguous sequence of characters within a string.

    Example 1:
    Input: num = "52"
    Output: "5"
    Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
    
    Example 2:
    Input: num = "4206"
    Output: ""
    Explanation: There are no odd numbers in "4206".
    
    Example 3:
    Input: num = "35427"
    Output: "35427"
    Explanation: "35427" is already an odd number.

Solution:
    Iterate from the last digit in num. If such digit is odd, we found the largest substring that is odd. Else, continue to the next digit. 

Complexity:
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def largestOddNumber(self, num: str) -> str:

        # Start from the end of num
        i = len(num) - 1

        # Iterate through all indices
        while i >= 0:

            # If the digit at the current index is odd, end the search
            if int(num[i]) % 2 == 1:
                break

            # Decrement the index
            i -= 1

        return num[0 : i + 1]

