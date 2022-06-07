""" 
Problem:
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.

    Example 1:
    Input: s = "aba"
    Output: true
    
    Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.
    
    Example 3:
    Input: s = "abc"
    Output: false

Solution:
    Create a left and a right pointer point to the start and the end of the string respectively. While left pointer is less than right pointer, check if chracters at the two pointers are equal. If it is not, skip either the left or the right pointer by 1 and check if the remaining characters are equal to its reverse. 

Complexity:
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # A left and a right pointers
        l, r = 0, len(s) - 1

        # While left is less than right
        while l < r:

            # If characters at the two pointers aren't equal
            if s[l] != s[r]:

                # Extract the remaining characters if skipped either the left or the right pointers by 1.
                skipL, skipR = s[l + 1 : r + 1], s[l:r]

                # Check if at least one of the string is equal to its reverse. 
                return skipL == skipL[::-1] or skipR == skipR[::-1]

            # Update pointers
            l, r = l + 1, r - 1

        return True


