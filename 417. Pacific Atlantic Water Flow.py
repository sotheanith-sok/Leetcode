"""
Problem:
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

    Example 1:
    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
    [0,4]: [0,4] -> Pacific Ocean 
        [0,4] -> Atlantic Ocean
    [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
        [1,3] -> [1,4] -> Atlantic Ocean
    [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
        [1,4] -> Atlantic Ocean
    [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
    [3,0]: [3,0] -> Pacific Ocean 
        [3,0] -> [4,0] -> Atlantic Ocean
    [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
        [3,1] -> [4,1] -> Atlantic Ocean
    [4,0]: [4,0] -> Pacific Ocean 
        [4,0] -> Atlantic Ocean
    Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
    
    Example 2:
    Input: heights = [[1]]
    Output: [[0,0]]
    Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Solution:
    Use dfs to find all nodes that contribute to the Atlantic Ocean and the Pacific Ocean. Then, find the intersection between the two sets to find all nodes which contribute to both oceans. 

Complexity:
    Time: O(mn)
    Space: O(mn)
"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        # Find the number of rows and cols
        m, n = len(heights), len(heights[0])

        # A helper function for calculating 4-directional neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # DFS starting from a list of node
        def dfs(starts):

            # Add the list of starting nodes to the stack
            stack = starts

            # Mark all starting nodes as visited
            visited = set(starts)

            # Iterate until the stack is empty
            while stack:

                # Pop a node
                row, col = stack.pop()

                # Calculate its neighboring node
                for dRow, dCol in directions:
                    neiRow, neiCol = row + dRow, col + dCol
                    
                    # If a neigboring node has its height taller than or equal to the current node and we haven't visit such node yet
                    if (
                        0 <= neiRow < m
                        and 0 <= neiCol < n
                        and (neiRow, neiCol) not in visited
                        and heights[row][col] <= heights[neiRow][neiCol]
                    ):
                        # Add such node to the stack
                        stack.append((neiRow, neiCol))

                        # Mark such node as visited
                        visited.add((neiRow, neiCol))

            # Return all visited nodes
            return visited

        # Find all nodes that contribute to the Pacific Ocean
        nodesP = dfs([(i, 0) for i in range(m)] + [(0, i) for i in range(n)])

        # Find all nodes that contribute to the Atlantic Ocean
        nodesA = dfs([(i, n - 1) for i in range(m)] + [(m - 1, i) for i in range(n)])

        # Using intersection to find all nodes that contirbute to both ocean
        nodes = nodesP.intersection(nodesA)

        # Return such nodes as a list
        return [list(pair) for pair in nodes]

