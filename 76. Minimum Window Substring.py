""" 
Problem:
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.

    Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    
    Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    
    Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

Solution:
    We can solve this problem using two pointers and a sliding window. We expand the window until it is valid and reduce the window until it isn't valid. Save the smallest window and return it. However, this approach will requires O(mn) because we have to compare windows to the target for every expansion and reduction. 

    We can avoid this comparison by maintaining a variable that keep track of how many character we still need and consider the target counter as what we still need.

    Iterate through all characters. At each iteration, if the current character is what we need, we decrement the number of character we still need by 1. Then, we decrement the current character count from the target counter. It is okay for count to go negative. 

    Once, we have all the character we need, we will remove the character that we don't need by increment its count in the target counter. Once, a character count is 0 (Only possible if we reach a character that exist in t), we have found the smallest possible windows ending at the current character. Save the overall smallest window and return it. 

Complexity:
    Time: O(m+n)
    Space: O(n)
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Get length of s and t
        m, n = len(s), len(t)

        # Initialize a counter to keep track of counts of character we still need and a variable to keep track of how many character is missing
        need, missing = Counter(t), n

        # Initialize two pointers for the result
        start, end = 0, 0

        # Initialize the left and right pointer of the sliding window
        l, r = 0, 1

        # Iterate until the right pointer reach the end of s (we will offset r by 1 to account for string slicing)
        while r <= m:

            # Decrement the number of missing characters if the current character is one of the character we need
            missing -= int(need[s[r - 1]] > 0)

            # Update the current character in the counter
            need[s[r - 1]] -= 1

            # If we have found all character
            if not missing:

                # Shrink the sliding window until we found the smallest possible window
                # This loop only end when we reached a character in t
                while l <= r and need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1

                # Save the window into the result if it is smaller than the previous result
                if not end or r - l <= end - start:
                    start, end = l, r

            # Increment the right pointer
            r += 1

        return s[start:end]

