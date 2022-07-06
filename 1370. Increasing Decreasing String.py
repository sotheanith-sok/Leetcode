""" 
Problem:
    You are given a string s. Reorder the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.
    In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

    Return the result string after sorting s with this algorithm.

    Example 1:
    Input: s = "aaaabbbbcccc"
    Output: "abccbaabccba"
    Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
    After steps 4, 5 and 6 of the first iteration, result = "abccba"
    First iteration is done. Now s = "aabbcc" and we go back to step 1
    After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
    After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
    
    Example 2:
    Input: s = "rat"
    Output: "art"
    Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Solution:
    We start by counting characters in a given string. Then, we store characters and their counts in a list and sort it alphabetically. Iterate through the list and append each character onto the result and update its count. Next, iterate through the list backward and follow the same rule. Skip any character that has a count of 0. Repeat the process until the length of the result is the same as the length of the given string.  

Complexity:
    Time: O(n) where O(n) for counting, O(26) for sorting, and O(26n) for building the result
    Space: O(1)
"""

from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:

        # Count characters and sort them alphabetically
        counts = sorted(Counter(s).items())

        # Initialize the result
        res = []

        # Keep track of if we want to go forward or backward
        reverse = False

        # Iterate until we used all character
        while len(res) != len(s):

            # Iterate through chracters in counts
            for i in range(len(counts)):

                # If reserve==False, i: 0,1,2,3,...
                # If reserve==True, i: -1,-2,-3,...
                i = -i - 1 if reverse else i

                # Get a character and its count
                char, count = counts[i]

                # If its count is 0, skip it
                if count == 0:
                    continue

                # Else, append the char to the result
                res.append(char)

                # Update the character count
                counts[i] = (char, count - 1)

            # Update iterative direction
            reverse = not reverse

        return "".join(res)

