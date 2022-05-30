"""
Problem:
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution:
    Use a left and a right pointers to create a sliding window. Create a set (list is slower when checking if a element is in the list) to store previous characters and a variable to store the maximum length of the subarray. Iterate through all characters in the string by incrementing the right pointer. At each iteration, while the character at the right pointer exists in the set, shrink the sliding window by removing the character at the left pointer from the set and incrementing the left pointer. Add the character at the right pointer to the set. Determine the maximum length by comparing previous value and the current size of the sliding window. 

Complexity:
    Time: O(n)
    Space: O(n)

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Store previous chars.
        prev_chars = set()

        # Initialize the left ptr and the max len.
        l, max_len = 0, 0

        # Iterate through all chars using the right ptr.
        for r in range(len(s)):

            # Shrink the sliding windows while the current char exists previously.
            while s[r] in prev_chars:
                prev_chars.remove(s[l])
                l += 1

            # Add the current char to the set.
            prev_chars.add(s[r])

            # Determine the maximum len.
            max_len = max(max_len, r - l + 1)

        return max_len
