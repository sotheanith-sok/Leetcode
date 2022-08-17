"""
Problem:
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    
    Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Solution:
    1. Stack
       Use a monotonically decreasing stack to store previous floor that we havn't found a right wall yet. 

       For every floor, if the height of the current floor is less than the height of floor on top of the stack, we will use such floor as the left wall of the current floor. Add current floor and the last seen floor at the height of previous floor on top of the stack onto the stack. 

       If the current floor is the same height as the floor on top of the stack, skip it. 

       Lastly, if the current floor is taller that the floor on top of the stack, pop such floor and use the current floor as the right wall and calculate the amount of water can be filled. Repeat until the floor on top of the stack is not less than the current floor. Then, add the current floor onto the stack.

    2. Two Pointers
        This approach relies on the fact that for some arbitrary floor, if we know the left max wall is less than a wall on the right, the left max wall is the bottleneck of the amount of water can be filled at that floor.  
        
        Start by initializing the left and right pointer to the start and end of heights. Set the max left wall and max right wall to zero. 
        
        While left and right pointers haven't meet, if the max left wall is less than the max right wall, we know that such wall will be the bottle neck of the floor at the left pointer. Calculate the water for such floor and increment the left pointer. 
        
        Else, we know that the max right wall is the bottleneck of the floor at the right pointer. Calculate the amount of water for such floor and decrement the right pointer. 

Complexity:
    Time: O(n)
    Space: O(n) for stack, O(1) for two pointers
"""

# Stack
class Solution:
    def trap(self, height: list[int]) -> int:

        # Initilaize a dict to keep track of last seen floor at each respective height
        seen = {}

        # Find the length of heights
        n = len(height)

        # Initialzie the stack
        stack = []

        # Initialzie the result
        res = 0

        # Iterate through all floors
        for r in range(n):

            # Save its index in the dict
            seen[height[r]] = r

            # While stack isn't empty
            while stack:

                # Find the floor and left wall on top of the stack
                floor, l = stack[-1]

                # If the height of such floor is greater than the height of the current floor, end the paring
                if height[floor] >= height[r]:
                    break

                # Pop a floor from the top of the stack
                stack.pop()

                # Calculate the amount of water
                res += (r - l - 1) * (min(height[l], height[r]) - height[floor])

            # If the current floor is the same height as the floor on top of the stack, skip such floor
            if stack and height[r] == height[stack[-1][0]]:
                continue

            # Else, add the current floor to the stack
            # If there is no value on top of the stack, use its height as the left wall
            stack.append((r, seen[height[stack[-1][0]]] if stack else r))

        return res


# Two pointers
class Solution:
    def trap(self, height: list[int]) -> int:

        # Initialize the max heights on the left of the left pointer and on the right of the right pointer
        lMax, rMax = 0, 0

        # Initialize the left and right pointers
        l, r = 0, len(height) - 1

        # Initialize the result
        res = 0

        # While the left and right pointers have not meet
        while l <= r:

            # If the left max is less than or equal to the right max
            if lMax <= rMax:

                # Update the left max height of the left pointer
                lMax = max(height[l], lMax)

                # Calculate the water that can be fill at the left pointer
                res += lMax - height[l]

                # Increment the left pointer
                l += 1

            # Else,
            else:

                # Update the right max height of the right pointer
                rMax = max(height[r], rMax)

                # Calculate the water that can be fill at the right pointer
                res += rMax - height[r]

                # Decrement the right pointer
                r -= 1

        return res
