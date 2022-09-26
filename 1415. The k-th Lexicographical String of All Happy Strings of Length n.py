"""
Problem:
    A happy string is a string that:

    consists only of letters of the set ['a', 'b', 'c'].
    s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
    For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

    Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

    Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

    Example 1:
    Input: n = 1, k = 3
    Output: "c"
    Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
    
    Example 2:
    Input: n = 1, k = 4
    Output: ""
    Explanation: There are only 3 happy strings of length 1.
    
    Example 3:
    Input: n = 3, k = 9
    Output: "cab"
    Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

Solution:
    Start by determining if we can pick kth string given a happy string of length n. Since we have 3 options initially, the range of happy string is between 0 and 3 * 2**(n-1) - 1. If k isn't in such range, return False. Else, continue to divide k by 2**(n-1) to decide on which character to pick next. Repeat until we pick n character. 

    Ex: n=3, k=9. 
    Thus, we want the 8th happy string

    n   options     k    pick(div)   nextK(mod)     res
    3   4           8    2           0              [c]
    2   2           0    0           0              [c, a]
    1   1           0    0           0              [c, a, b]

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        # Decrement k by one for 0th base indices.
        k -= 1

        # Initialize the result
        res = [""]

        # Next options based on a given character
        nextString = {
            "": ["a", "b", "c"],
            "a": ["b", "c"],
            "b": ["a", "c"],
            "c": ["a", "b"],
        }

        # If we can't pick kth string given a happy string of length n, return False
        if k >= 3 * 2 ** (n - 1):
            return ""

        # Else, pick n characters
        for n in range(n - 1, -1, -1):

            # Decide on which character to pick and next k
            pick, k = divmod(k, 2 ** n)

            # Append the picked character to the result
            res.append(nextString[res[-1]][pick])

        return "".join(res)
