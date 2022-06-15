""" 
Problem:
    Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum number of instances that can be formed.

    
    Example 1:
    Input: text = "nlaebolko"
    Output: 1
    
    Example 2:
    Input: text = "loonbalxballpoon"
    Output: 2
    
    Example 3:
    Input: text = "leetcode"
    Output: 0

Solution:
    We will count how many occurrences of each character in the given string. Then, we check if we can form 1,2,3,... of the word "balloon" and return the result.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {}

        for c in text:
            map[c] = map[c] + 1 if c in map else 1

        characters = [("b", 1), ("a", 1), ("l", 2), ("o", 2), ("n", 1)]

        i = 0

        while True:
            for c, count in characters:
                if c not in map or map[c] < count * (i + 1):
                    return i

            i += 1


