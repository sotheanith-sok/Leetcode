"""
Problem:
    A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

    Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

    Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

    Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

    Example 1:
    Input: satisfaction = [-1,-8,0,5,-9]
    Output: 14
    Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
    Each dish is prepared in one unit of time.
    
    Example 2:
    Input: satisfaction = [4,3,2]
    Output: 20
    Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
    
    Example 3:
    Input: satisfaction = [-1,-4,-5]
    Output: 0
    Explanation: People do not like the dishes. No dish is prepared.

Solution:
    Since we can cook dishes in any order, we can be greedy and cook dishes with the higest satisfaction level last. Start by sorting all satisfaction level. Next, calculate the like-time coefficient if we were to cook all dishes. Then, iterate through all dishes from the left, discard each dish, and recalculate the like-time coefficient. Return the largest coefficient. 

    To avoid recalculating the like-time coefficient everytime we discard each dishes, we can take away one occurence of each remaining dishes from the current like-time coefficient.

    Ex: satisfaction = [a, b, c, d]

    All dishes          = a*1 + b*2  + c*3 + d*4  
    Discard 1st dish    = (a*1 + b*2  + c*3 + d*4 )     - (a + b + c + d)   = b*1 + c*2 + d*3
    Discard 2nd dish    = (b*1 + c*2 + d*3)             - (b + c + d)       = c*1 + d*2
    Discard 3rd dish    = (c*1 + d*2)                   - (c + d)           = d*1
    Discard 4th dish    = (d*1)                         - (d)               = 0
 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:

        # Get the number of dishes
        n = len(satisfaction)

        # Sort all dishes based on its satisfaction level
        satisfaction.sort()

        # Calculate the sum of all satisfaction levels
        total = sum(satisfaction)

        # Calculate the like-time coefficient if we are to cook all dishes
        coefficient = sum(i * level for i, level in zip(range(1, n + 1), satisfaction))

        # Initialize the result
        res = coefficient

        # Iterate through all dishes
        for level in satisfaction:

            # Recalculate the like-time coefficient if we are to discard the current dish
            coefficient -= total
            total -= level

            # Update the result
            res = max(res, coefficient)

        return res
