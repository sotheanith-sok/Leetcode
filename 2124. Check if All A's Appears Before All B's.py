"""
Problem:
    Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

    Example 1:
    Input: s = "aaabbb"
    Output: true
    Explanation:
    The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
    Hence, every 'a' appears before every 'b' and we return true.
    
    Example 2:
    Input: s = "abab"
    Output: false
    Explanation:
    There is an 'a' at index 2 and a 'b' at index 1.
    Hence, not every 'a' appears before every 'b' and we return false.
    Example 3:
    Input: s = "bbb"
    Output: true
    Explanation:
    There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

Solution:
    Find the last occurence of a and the first occurence of b. Return true if a < b.

Complexity:
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def checkString(self, s: str) -> bool:

        # Find the last occurence of a and the first occurence of b
        a, b = s.rfind("a"), s.find("b")

        # Return true if a or b doesn't exist in s or all a comes before all b
        return a == -1 or b == -1 or a < b

