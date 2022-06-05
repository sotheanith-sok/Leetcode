""" 
Problem:
    You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

    The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

    Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

    Example 1:
    Input: grid = [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.
    
    Example 2:
    Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation: The final route is shown.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Solution (Dijkstra's Algorithm):
    We will perform a bfs search on the graph. To start with it, we will add the (0,0) node and its cost to the min heap (sorted by the cost). Until we reach the (n-1,n-1) node, we pop a node from the heap a. Then, for every unvisited neighbor, we pick the max between the current node cost and the neighbor node cost and add that neighbor node to the min heap and mark it as visited. Repeat the process.   

Problem:
    Time: O(n**2)
    Space: O(n**2)

"""
import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        # Get the size of the grid
        N = len(grid)

        # Set used to store visited node
        visited = set()

        # A helper list used for directions
        direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        # create and add the first node into the heap
        heap = [[grid[0][0], 0, 0]]
        visited.add((0, 0))

        while heap:

            # Pop the least cost node from the heap
            time, row, col = heapq.heappop(heap)

            # # If we marks a node when we visit it only, the size of the heap will increase exponentially.
            # visited.add((row, col))

            # If we reach (n-1, n-1) node, return the cost
            if row == N - 1 and col == N - 1:
                return time

            # Add all unvisited neighbors to the heap
            for drow, dcol in direction:

                # Calculate neighbors coordinates
                neiRow, neiCol = row + drow, col + dcol

                # Only add unvisited neighbors that aren't out of bound to the heap.
                if (
                    0 <= neiRow < N
                    and 0 <= neiCol < N
                    and (neiRow, neiCol) not in visited
                ):
                    # Push neighbors onto the heap.
                    heapq.heappush(
                        heap, [max(time, grid[neiRow][neiCol]), neiRow, neiCol]
                    )

                    # We need to mark all neighbors as visted right away because, without marking it here, mutiple nodes can add their common neighbors multiple time into the heap. If we marks a node when we visit it only, the size of the heap will increase exponentially.
                    visited.add((neiRow, neiCol))
