""" 
Problem:
    Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

    Example 1:
    Input: s = "00110110", k = 2
    Output: true
    Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
    
    Example 2:
    Input: s = "0110", k = 1
    Output: true
    Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

    Example 3:
    Input: s = "0110", k = 2
    Output: false
    Explanation: The binary code "00" is of length 2 and does not exist in the array.
Solution:
    Instead of generating all possible combinations of binary code of size k and check if all of those combinations are a substring of the given string s (it takes O((2**k)n) to this), we can count all uniques substring of s with size k. If the count of all possible substrings is equal to the count all possible combinations of binary code, then we know that every binary code of length k is a substring of s.  

Complexity:
    Time: O(n)
    Space: O(1)
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # Use set since we want all uniques substring.
        substrings = set()

        # Generate all substrings of size k.
        for i in range(len(s) - k + 1):
            substrings.add(s[i : i + k])

        # Check if the size of unique substrings is equal to the count of possible combinations of binary code of size k.
        return len(substrings) == 2 ** k

