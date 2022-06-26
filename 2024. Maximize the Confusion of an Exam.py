"""
Problem:
    A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

    You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

    Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
    Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

    Example 1:
    Input: answerKey = "TTFF", k = 2
    Output: 4
    Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
    There are four consecutive 'T's.
    
    Example 2:
    Input: answerKey = "TFFT", k = 1
    Output: 3
    Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
    Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
    In both cases, there are three consecutive 'F's.
    
    Example 3:
    Input: answerKey = "TTFTTFTT", k = 1
    Output: 5
    Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
    Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
    In both cases, there are five consecutive 'T's.

Solution:
    Similar to leetcode 424, we will use a sliding window to solve this problem. Keep expanding the window as long as it is valid. A window is valid if its most frequent character is at most k less than the size of the window. Shrink the window if it isn't valid. Noted that since we only have to find a largest possible window, we only have to update the max frequency if we found a larger one.  

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # A map to keep track of characters and their counts
        count = {}

        # Variables to keep track of the result and the most frequent character
        res, maxf = 0, 0

        # Initialize the left pointer
        l = 0

        # Iterate through all characters using the right pointer
        for r in range(len(answerKey)):

            # Update the count of the character at the right pointer
            count[answerKey[r]] = (
                count[answerKey[r]] + 1 if answerKey[r] in count else 1
            )

            # Update the max frequent character if the character at the right pointer has a larger count than previous characters
            maxf = count[answerKey[r]] if count[answerKey[r]] > maxf else maxf

            # Continue to shrink window until it is valid
            while r - l + 1 - maxf > k:
                count[answerKey[l]], l = count[answerKey[l]] - 1, l + 1

            # Update the result if we found a larger window
            res = r - l + 1 if r - l + 1 > res else res

        return res

