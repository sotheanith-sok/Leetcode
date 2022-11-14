""" 
Problem:
    On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

    A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

    Example 1:
    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5
    Explanation: One way to remove 5 stones is as follows:
    1. Remove stone [2,2] because it shares the same row as [2,1].
    2. Remove stone [2,1] because it shares the same column as [0,1].
    3. Remove stone [1,2] because it shares the same row as [1,0].
    4. Remove stone [1,0] because it shares the same column as [0,0].
    5. Remove stone [0,1] because it shares the same row as [0,0].
    Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
    
    Example 2:
    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3
    Explanation: One way to make 3 moves is as follows:
    1. Remove stone [2,2] because it shares the same row as [2,0].
    2. Remove stone [2,0] because it shares the same column as [0,0].
    3. Remove stone [0,2] because it shares the same row as [0,0].
    Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
    
    Example 3:
    Input: stones = [[0,0]]
    Output: 0
    Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

Solution:
    Rather than consider how many stones we can remove, we should consider how many group of stones we can form. Then, for each group, we can remove all except one stone. Thus, start by building an adjacency list for rows and cols. Then, dfs through all stones and see how many group we can form. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:

        # Build adjacency lists for both rows and cols
        rows, cols = defaultdict(list), defaultdict(list)
        for col, row in stones:
            rows[col].append(row)
            cols[row].append(col)

        # Group all stones using DFS
        # Initialzie a set to keep track of visited stone
        visited = set()

        # Initialize a number of group found
        group = 0

        # Iterate through all stones
        for col, row in stones:

            # If we already visited the current stone, skip it
            if (row, col) in visited:
                continue

            # Else, we have found a new group
            group += 1

            # Add the current stone into the stack
            stack = [(row, col)]
            visited.add((row, col))

            # Iterate until stack is empty
            while stack:

                # Pop a stone
                row, col = stack.pop()

                # Add all unvisited stones at the same col into the stack
                for nRow in rows[col]:
                    if (nRow, col) not in visited:
                        visited.add((nRow, col))
                        stack.append((nRow, col))

                # Add all unvisted stones at the same row into the stack
                for nCol in cols[row]:
                    if (row, nCol) not in visited:
                        visited.add((row, nCol))
                        stack.append((row, nCol))

        # Return the number of removed stones
        return len(stones) - group
