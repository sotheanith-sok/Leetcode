"""
Problem:
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    

    Example 1:

    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.
    Example 2:

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

Solution:
    Use Knuth–Morris–Pratt algorithm to solve this problem. The algorithm works in two stages

    1. Longest Prefix-Surfix (LPS)
    Start by calculating the lps ending at each character in the needle. Initlaize two pointers, one to keep track of current index in needle and another to keep track of the current lps so far. For each character in the needle, if the current character can increase the current lps increment lps and i by 1. Else, we will decrement lps to the previous lps at lps-1. Repeat until we found a matching character or lps reaches 0.

    2. Pattern Matching
    Use two pointers i and j  to keep track of the current characters of both haystack and needle. If both characters are equal, increment i and j. Else, if j>0, decrement j to lps[j-1] because lps will tell us about the length of longest prefix-subfix from 0 to j-1 and thus, we can skip some comparision. Else, incrmrent i to 1.

    Ex. Given haystack = "mississippi", needle = "issip"

    1. Longest Prefix-Surfix
    i   lsp     charAt(i)   charAt(lsp)     nextlsp
    1   0       s           i               0
    2   0       s           i               0
    3   0       i           i               1
    4   1       p           s                   
    4   0       p           i               0

    lps = [0,0,0,1,0]

    2. Pattern Matching

    i           0   1   2   3   4   5   6   7   8
    
    j           0   0   1   2   3   4
                                    1   2   3   4
    
    charAt(i)   m   i   s   s   i   s   s   i   p   p   i
    
    charAt(j)   i   
                    i   s   s   i   p
                                    s   s   i   p

    At i == 5 and j==4, charAt(i) == s != charAt(j) == p. Thus, we find lps of the previous substring. lps[3] is 1 so we can skip first character. Thus, j is updated to character to 1. 
    
Complexity:
    Time: O(m + n) where m and n are lengths of haystack and needle respectively
    Space: O(n)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Get lengths of haystack and needle
        m, n = len(haystack), len(needle)

        # 1. Calculate lps of all characters in needle
        # Initialize a list of store lps ended at all characters in needle
        lpsList = [0] * n

        # Initialize two variables: one to iterate through all characters in needle and another to keep track of the current lps
        j, lps = 1, 0

        # Iterate through all characters
        while j < n:

            # If the current character and character next to the lps is equal, the current character will increase the length of lps
            if needle[j] == needle[lps]:

                # Increment the current lps
                lps += 1

                # Save the current lps ended at j
                lpsList[j] = lps

                # Increment j
                j += 1

            # Else
            else:

                # If lps isn't 0, set lps to the previous lps at lps-1
                if lps > 0:
                    lps = lpsList[lps - 1]

                # Else, incrment j by 1
                else:
                    j += 1

        # 2. Pattern Matching

        # Initialize two variables to keep track of characters of haystack and needle
        i, j = 0, 0

        # While we haven't reach the end of each string
        while i < m and j < n:

            # If current characters are equal, continue to next pair
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1

            # Else,
            else:

                # Check if there is previous substring
                if j > 0:

                    # If yes, set the j pointer to the next character of the prefix part of the lps of such substring
                    j = lpsList[j - 1]

                # Else, increment i
                else:
                    i += 1

        # Return the index if we are able to reach the end of needle. Else, return -1
        return i - j if j == n else -1

