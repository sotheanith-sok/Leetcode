"""
Problem:
    You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

    To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

    For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
    You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

    Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

    Example 1:
    Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
    Output: true
    Explanation: The allowed triangular patterns are shown on the right.
    Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
    There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
    
    Example 2:
    Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
    Output: false
    Explanation: The allowed triangular patterns are shown on the right.
    Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.

Solution:
    Use dfs to search through all possible next state from a given state. If the length of the state reaches 1, we have succesfully build the pyramid. If length of next state is 1 less than the length of the current state, we can move to the next level. Else, if we picked length of state - 1 node and we couldn't go to next level, this route won't lead to the solution. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict
from functools import lru_cache


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:

        # Create a states mapping from two source nodes to one destination node
        states = defaultdict(list)

        # Add all connection into the states
        for nodes in allowed:
            states[(nodes[0], nodes[1])].append(nodes[2])

        @lru_cache(None)
        def dfs(i, state, nxt):

            # If we have 1 node left, we have succesfully build the pyramid and thus, we return True
            if len(state) == 1:
                return True

            # If the number of nodes in the next states is one less than the current states, we can go to next level
            if len(state) == len(nxt) + 1:
                return dfs(0, nxt, "")

            # If we unable to go to next level after picking length of current states - 1 nodes, return False
            if i == len(state) - 1:
                return False

            # Build next states from all possibles node giving two source nodes at i and i + 1
            for c in states[(state[i], state[i + 1])]:
                if dfs(i + 1, state, nxt + c):
                    return True

            return False

        return dfs(0, bottom, "")

