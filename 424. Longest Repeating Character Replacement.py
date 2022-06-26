""" 
Problem:
    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.
    
    Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.

Solution:
    We will use a sliding windows to solve this problem. For any given sliding windows, we will keep expanding it as long as the window is valid and we will shrink it if it is no longer valid. To check if a window is valid, we have to ensure that the most common characters is at most k less than the size of the window( size of windows - most frequent character <=k). It is worth noting that we only have to update the most frequent character if there is a character that is more frequent than the current frequent character since a smaller frequent character will only be valid if the window size is smaller. 

Complexity:
    Time: O(n)
    Space: O(1) since we can have at most 26 characters
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Intialize the result and max frequent variables
        res, maxf = 0, 0

        # Initialize the left and right pointers.
        l, r = 0, 0

        # Initialize a map to keep track of characters and their counts
        count = {}

        # Iterate the right pointer until the end of the string
        for r in range(len(s)):

            # Increment the count of the character at the right pointer
            count[s[r]] = count[s[r]] + 1 if s[r] in count else 1

            # Update the frequency if the current count is larger than the previous count.
            maxf = count[s[r]] if count[s[r]] > maxf else maxf

            # Shrink the window by increment the left pointer if it isn't valid
            while (r - l + 1) - maxf > k:
                count[s[l]], l = count[s[l]] - 1, l + 1

            # Update the result if we found a larger window
            res = r - l + 1 if r - l + 1 > res else res

        return res

