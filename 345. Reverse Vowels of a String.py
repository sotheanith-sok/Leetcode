""" 
Problem:
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

    Example 1:
    Input: s = "hello"
    Output: "holle"

    Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Solution:
    Run two pointers from the start and end of s. Swap every pair of vowels until both pointers meet. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:

        # Get length of s
        n = len(s)

        # Convert s into a list for O(1) editing
        s = list(s)

        # Initialize both pointers
        l, r = 0, n - 1

        # Create a set to check if a character is a vowel
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        # Iterate until both pointers meet
        while l < r:

            # Increment the left pointer if it doesn't point to a vowel
            if s[l] not in vowels:
                l += 1
                continue

            # Decrement the right pointer if it doesn't point to a vowel
            if s[r] not in vowels:
                r -= 1
                continue

            # Swap both vowels
            s[l], s[r] = s[r], s[l]

            # Update both pointers
            l, r = l + 1, r - 1

        return "".join(s)
