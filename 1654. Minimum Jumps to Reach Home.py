""" 
    A certain bug's home is on the x-axis at position x. Help them get there from position 0.

    The bug jumps according to the following rules:

    It can jump exactly a positions forward (to the right).
    It can jump exactly b positions backward (to the left).
    It cannot jump backward twice in a row.
    It cannot jump to any forbidden positions.
    The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

    Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

    
    Example 1:
    Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
    Output: 3
    Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
    
    Example 2:
    Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
    Output: -1
    
    Example 3:
    Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
    Output: 2
    Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.

Solution:
    We can solve this problem using BFS. For each node, we can either go forward "a" steps or go backward "b" steps. However, since we can't go backward back to back, we also have keep track of if we reach a node due to backwarding from the previous node. The main problem is to determine the largest possible node. Without it, our queue will spiral into infinity as we keep moving forward "a" steps. Thus, we will cap the largest node at a+b+max(x, max(forbidden)).

    Intuition:
    1. If a>=b, then there is no point in search pass x as we can never go back.
    2. If a<b, then we will search pass x. Since a<b, we know that we can always go back but there is some nodes that are forbidden. Thus, we should at least search pass that. Then, from there if we go pass a+b and try to reduce back to x, we will meet with a lot of repeated node and thus, there is no point in going pass it. 
    
    https://pic.leetcode-cn.com/1605602721-qSbxPs-image.png
    
    Full explaination for the cap: 
    https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/978357/C%2B%2B-bidirectional-BFS-solution-with-proof-for-search-upper-bound 

Complexity:
    Time: O(n) where n is the cap = a+b+max(x,max(forbidden))
    Space: O(n)
"""


from collections import deque


class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:

        # Convert forbidden list from a list to a set
        forbidden = set(forbidden)

        # Initialize the largest possible node
        cap = a + b + max(x, max(forbidden))

        # Initialize the queue and the first node to it
        queue = deque()
        queue.append((0, False))

        # Mark the first node as forbidden
        forbidden.add(0)

        # Initialize the cost
        cost = 0

        # Perform BFS
        while queue:

            # Get the number of nodes in this level
            n = len(queue)

            # Process all nodes
            for _ in range(n):

                # Pop a node
                i, back = queue.popleft()

                # If we reach node x, return the cost
                if i == x:
                    return cost

                # If we pass the cap, continue to the next node
                if i > cap:
                    continue

                # Add the next node if we are to move backward to the queue
                if not back and i - b >= 0 and i - b not in forbidden:
                    queue.append((i - b, True))
                    forbidden.add(i - b)

                # Add the net node if we are to move forward to the queue
                if i + a not in forbidden:
                    queue.append((i + a, False))
                    forbidden.add(i + a)

            # Increment the cost
            cost += 1

        return -1

