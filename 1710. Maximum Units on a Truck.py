"""
Problem:
    You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.
    You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

    Return the maximum total number of units that can be put on the truck.

    Example 1:
    Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    Output: 8
    Explanation: There are:
    - 1 box of the first type that contains 3 units.
    - 2 boxes of the second type that contain 2 units each.
    - 3 boxes of the third type that contain 1 unit each.
    You can take all the boxes of the first and second types, and one box of the third type.
    The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
    
    Example 2:
    Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
    Output: 91

Solution:
    Sort boxes by their units and then greedily add boxes into the truck until we added all boxes or we run out of space in the truck.

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:

        # Sort boxes by their units in an ascending order since poping from the end of a stack is O(1)
        boxTypes.sort(key=lambda x: x[1])

        # Initialize the result
        res = 0

        # Iterate if we still have unloaded boxes and truck isn't full
        while boxTypes and truckSize > 0:

            # Pop a box and its units from the stack
            count, weight = boxTypes.pop()

            # Add the units to the result. You either add all boxes of this type or whatever left of the capacity of the truck and thus, we can do min(count, truckSize)
            res += min(count, truckSize) * weight

            # Update the capacity
            truckSize -= min(count, truckSize)

        return res
