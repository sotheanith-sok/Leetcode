""" 
Problem:
    Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

    Example 1:
    Input: s = "aaabb", k = 3
    Output: 3
    Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
    
    Example 2:
    Input: s = "ababbc", k = 2
    Output: 5
    Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Solution:
    Solve this problem using a sliding window. However, the main question is when should we increase or decrease the sliding window. A solution is to fix the number of unique character is our substring. Thus, we will iterate through all possible number of allowed unique characters starting from 1 and up to the number of unique character in the given string. At each iteration, we will keep track of the frequency of each character and note the number of unique character that occur at least one and at least k times. We will continue to expand the sliding window as long as the number of unique character that occur at least one is less than or equal to the number of allowed unique characters. And, we will decrease the sliding window if the condition no longer true. Once, the the number of allowed unique characters is equal to the number of unique character that occur at least one and the number of unique character that occur at least k, we have found a valid substring.   

Complexity:
    Time: O(26n)
    Space: O(1)
"""

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # Initialize the result
        res = 0

        # Iterate through all possible allowed unique characters
        for allowedUnique in range(1, len(Counter(s)) + 1):

            # Initialize the left pointer and the right pointer
            l, r = 0, 0

            # Initialize varaibles to keep track of characters that appear at least 1 (a unique number) and at least k
            numsUnique, numsAtLeastK, = 0, 0

            # Initialize the hashmap to keep track of frequency
            freq = {}

            # Iterate until the right pointer reach the end of the string
            while r < len(s):

                # If a window contains unique characters more than allowed, shrink it until the window is valid
                while numsUnique > allowedUnique:

                    # Decrement the number of unique character if the character at the left pointer appears exactly 1 time
                    if freq[s[l]] == 1:
                        numsUnique -= 1

                    # Decrement the number of character that appeared at least k times if the character at the left pointer appears exactly k time.
                    if freq[s[l]] == k:
                        numsAtLeastK -= 1

                    # Decrement the frequency of the character at the left pointer
                    freq[s[l]] -= 1

                    # Increment the left pointer
                    l += 1

                # Increment the frequency of the character at the right pointer
                freq[s[r]] = freq[s[r]] + 1 if s[r] in freq else 1

                # Increment the number of unique character if the character at the right pointer appears exactly 1 time
                if freq[s[r]] == 1:
                    numsUnique += 1

                # Increment the number of chracter that appeared at least k time if the character at the right pointer appears exactly k times
                if freq[s[r]] == k:
                    numsAtLeastK += 1

                # If we found a valid substring aka the number of allowed unique character is equal to the number of unique character and the number of character that appeared at least k time,
                if numsUnique == numsAtLeastK == allowedUnique:

                    # Update the result
                    res = max(res, r - l + 1)

                # Increment the right pointer
                r += 1

        return res

