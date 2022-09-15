"""
Problem:
    An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

    Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

    Example 1:
    Input: changed = [1,3,4,2,6,8]
    Output: [1,3,4]
    Explanation: One possible original array could be [1,3,4]:
    - Twice the value of 1 is 1 * 2 = 2.
    - Twice the value of 3 is 3 * 2 = 6.
    - Twice the value of 4 is 4 * 2 = 8.
    Other original arrays could be [4,3,1] or [3,1,4].
    
    Example 2:
    Input: changed = [6,3,0,1]
    Output: []
    Explanation: changed is not a doubled array.
    
    Example 3:
    Input: changed = [1]
    Output: []
    Explanation: changed is not a doubled array.

Solution:
    A number is a part of the orignal array if there exists another number that double such number. Thus, we should try to pair a smallest number first since it can only be the original number; not the double of another number. 

    Start by counting all numbers and their occurrences. Iterate through all sorted unique numbers. If the current number hasn't been pair with another number, check if there exists another number that double such number and we haven't use both numbers yet. If yes, add the orignal number to the result and decrement counts of both numbers. Lastly, remove any number with its count of 0 from the counter. Return the result if we paired all numbers. Else, return empty list. 

    Do note that if the current number is 0, we should check that there exists at least 2 occurrences of such number before adding it to the result

Complexity:
    Time: O(nlogn) where n is the number of unique changed
    Space: O(n)
"""

from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        # Count all numbers
        counts = Counter(changed)

        # Initialize the result
        res = []

        # Iterate through all numbers
        for num in sorted(counts):

            # If the current number hasn't been paired yet and there is another unpair number that double it, pair both numbers
            if num in counts and (
                (num == 0 and counts[num] >= 2) or (num != 0 and num * 2 in counts)
            ):

                # Calculate how many occurence of both numbers can be paired together
                occurence = (
                    min(counts[num], counts[num * 2]) if num != 0 else counts[num] // 2
                )

                # Add number to the result
                res += [num] * occurence

                # Decrement counts of both numbers
                counts[num] -= occurence
                counts[num * 2] -= occurence

                # Remove the current number from the counter if its count is 0
                if num in counts and counts[num] == 0:
                    counts.pop(num)

                # Remove the double of the current number from the counter if its count is 0
                if num * 2 in counts and counts[num * 2] == 0:
                    counts.pop(num * 2)

        # Return result if we paired all numbers
        # Else, return empty list
        return res if not counts else []
