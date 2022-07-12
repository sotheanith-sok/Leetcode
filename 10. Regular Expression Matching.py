"""
Problem:
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    
    Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    
    Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    
    Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

Solution:
    Solve this problem using bottom-up dynamic programming approach similar to editing distance. Initialize the 2d arrays of size len(s) + 1 by len(p) + 1. The first row and column represents an empty string and an empty pattern. For any indices i, j:

        # Case 1: We found a matching character pair or a wild card in the pattern.
        1. If charS[i] == charP[j] or charP[j] == ".", 
            dp[i][j] = dp[i-1][j-1]

        # Case 2: If we found a matching zero or more of the preceding element  
        2. Else, if charP[j] == "*",

            # Case 2.1: If the preceding element doesn't not match the character at i, we assume 0 for the preceding element.
            2.1 If charS[i] != charP[j] and charP[j] != ".",
                    dp[i][j] = dp[i][j-2]

            # Case 2.2: If the preceding element match the character at i, 
            2.2 Else if charS[i] == charP[j] or charP[j] == ".",
                    dp[i][j] = 
                        dp[i-1][j] or  # Check for multiple occurrence of the preceding element 
                        dp[i][j-1] or  # Check for a single occurence of the preceding element
                        dp[i][j-2]     # Check for 0 occurence of the preceding element

Complexity:
    Time: O(mn)
    Space: O(mn)
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Get length of string and pattern
        m,n = len(s), len(p)

        # Intialize the cache
        cache = [[False for _ in range(n+1)] for _ in range(m+1)]

        # Index (0,0) is for an empty string and an empty pattern
        cache[0][0] = True

        # Intialize the base case when a string is empty
        for j in range(n):
            if p[j]=="*":
                cache[0][j+1] = cache[0][j-1] 

        # Iterate through the cache and fill it in
        for i in range(m):
            for j in range(n):

                # When we found a matching pair
                if s[i] == p[j] or p[j] =='.':

                    # cache[i,j] = cache[i-1][j-1] => Assume the same result as the i-1 and j-1 
                    cache[i+1][j+1] = cache[i][j]

                # When we found a repeated character
                elif p[j]=="*":

                    # If we can't match the current character at i with the previous character at j-1
                    if s[i] !=p[j-1] and p[j-1] != '.':

                        # cache[i][j] = cache[i][j-2] => assume 0 occurence
                        cache[i+1][j+1] = cache[i+1][j-1]

                    # Else, we can match the current character at i with previous character at j-1
                    elif s[i] == p[j-1] or p[j-1]==".":
                        
                        # We have to check three cases:
                        # 1. 0 occurence: cache[i][j] = cache[i][j-2]
                        # 2. 1 occurence: cache[i][j] = cache[i][j-1]
                        # 3. Multiple occurence: cache[i][j] = cache[i-1][j]
                        cache[i+1][j+1] = cache[i][j+1] | cache[i+1][j] | cache[i+1][j-1]   

        return cache[-1][-1]

