""" 
Problem:
    Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.

    Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

    Example 1:
    Input: s = "the sky is blue"
    Output: "blue is sky the"
    
    Example 2:
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
    
    Example 3:
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Solution:
    Let pretend s is an array of characters. We will reverse all words using the following steps:
        Ex: given s = "  hello world  "

        1. Shift all characters to the left (aka remove all leading whitespace)
            ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'd', ' ', ' ']

        2. Remove all tailing characters that we don't need
            ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'

        3. Reverse all words
            ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']

        4. Reverse each words
            ['w', 'o', 'r', 'l', 'd', ' ', 'h', 'e', 'l', 'l', 'o']

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)

        # 1. Shift all characters to the left (aka remove all leading whitespace)
        l = 0
        for r in range(len(arr)):
            if (r == 0 and arr[r] == " ") or (r > 0 and arr[r] == arr[r - 1] == " "):
                continue
            arr[l] = arr[r]
            l += 1

        # 2. Remove all tailing characters that we don't need
        while len(arr) > l or arr[-1] == " ":
            arr.pop()

        # 3. Reverse all words
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

        # 4. Reverse each word
        l = r = k = 0
        while k <= len(arr):

            # Find the end of each word
            if k < len(arr) and arr[k] != " ":
                k += 1
                continue

            # Update the right pointer
            r = k - 1

            # Reverse all words
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1

            # Update the left pointer
            l = k + 1

            k += 1

        return "".join(arr)
