"""
Problem:
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
    To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

    For example, the saying and conversion for digit string "3322251":

    Given a positive integer n, return the nth term of the count-and-say sequence.

    Example 1:
    Input: n = 1
    Output: "1"
    Explanation: This is the base case.
    
    Example 2:
    Input: n = 4
    Output: "1211"
    Explanation:
    countAndSay(1) = "1"
    countAndSay(2) = say "1" = one 1 = "11"
    countAndSay(3) = say "11" = two 1's = "21"
    countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Solution:
    For some arbritary n, you will say the "say" of n - 1. Start from 1 to n. Use a list to store the next "say". 
    For every next "say", iterate through all character of the current "say". If the list of the next "say" is empty or the current chracter is different than previous character, add the count of 1 and the current character to the list. Else, increment the count by 1. 

    ie. countAndSay(1) = 1
        countAndSay(2) = 11
        countAndSay(3) = 21
        countAndSay(4) = 1211
        countAndSay(5) = 111221

Complexity:
    Time: O(n!)
    Space: O(n)
"""


class Solution:
    def countAndSay(self, n: int) -> str:

        # Initialzie the basecase
        res = ["1"]

        # Generate next "say" from 2 to n
        for _ in range(2, n + 1):

            nextRes = []

            # Iterate through all chracters of the current "say"
            for c in res:

                # If the list is empty or the current character is different from the previous character
                if not nextRes or nextRes[-1] != c:

                    # Add the count of 1 and the current character to the list
                    nextRes.extend(["1", c])

                    continue

                # Else, increment the count
                nextRes[-2] = str(int(nextRes[-2]) + 1)

            res = nextRes

        return "".join(res)

