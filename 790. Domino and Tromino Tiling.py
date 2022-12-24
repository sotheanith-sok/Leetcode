""" 
Problem:
    You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

    Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

    In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

    Example 1:
    Input: n = 3
    Output: 5
    Explanation: The five different ways are show above.
    
    Example 2:
    Input: n = 1
    Output: 1

Solution:
    Let i be the index that we need to put the next tile and "extrude" be the length of previous placed tile that extrude from the current index. We will continue to fill until we reach n-th index. Return 1 if we perfectly filled in all cells else 0. Initially i and extrude are 0.

    Tiles: ┃ ┏━ ┗━ ━┓ ━┛ ━━

    i   extrude     possibleNextShapes          nextI       nextExtrude
    i   0           ┃                           i+1         0
                    ┏━ ┗━                       i+1         1
                    ━━                          i           2
    i   1           ━┛ or ━┓                    i+2         0
                    ━━                          i+1         1
    i   2           ━━                          i+2         0

Complexity:
    Time: O(n)
    Space: O(n)
"""


from functools import lru_cache


class Solution:
    def numTilings(self, n: int) -> int:

        # Sum up all possible tile configuration that perfectly filled all cells
        @lru_cache(None)
        def dp(i, extrude):

            # If we filled all cells
            if i >= n:

                # Return 1 if we filled all cells perfectly else 0
                return 1 if i == n and extrude == 0 else 0

            # 4 possible tiles: ┃ and ┏━ and ┗━ and ━━
            if extrude == 0:
                return dp(i + 1, 0) + 2 * dp(i + 1, 1) + dp(i, 2)

            # 3 possible tiles: ━━ and (━┓ or ━┛)
            if extrude == 1:
                return dp(i + 1, 1) + dp(i + 2, 0)

            # 1 possible next tile: ━━
            if extrude == 2:
                return dp(i + 2, 0)

        return dp(0, 0) % (10**9 + 7)
