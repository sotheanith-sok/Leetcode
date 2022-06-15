""" 
Problem:
    You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    float("inf") - float("inf")inity means an empty room. We use the value 231 - 1 = 2147483647 to represent float("inf") as you may assume that the distance to a gate is less than 2147483647.
    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with float("inf").

    Example: 
    Given the 2D grid:
    float("inf")  -1  0  float("inf")
    float("inf") float("inf") float("inf")  -1
    float("inf")  -1 float("inf")  -1
    0  -1 float("inf") float("inf")

    After running your function, the 2D grid should be:
    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4

Solution:
    Find a starting node(distance == 0) and start a bfs from there. For subsequence neighborig nodes, update their distance such that it is 1 more than the previous node. Only update a distance to a given node if it is less than existing distance. Since distance started at 0 and keep increasing, the wall node (distance == -1) will never get override. If any node contain is unreachable, it will never get its value updated. 

Complexity:
    Time: O(m . n)
    Space: O(m . n)

"""


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:

        # Find the length of the row and the col of the graph.
        rows, cols = len(rooms), len(rooms[0])

        # A healper function used for checking neighboring nodes.
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        # Iterate through every nodes.
        for row in range(rows):
            for col in range(cols):

                # If it isn't a starting node, we move on to the next node.
                if rooms[row][col] != 0:
                    continue

                # Add a starting node to the queue
                queue = [[0, row, col]]

                # While there is an unvisited node
                while queue:

                    # Pop the next unvisited node.
                    dst, row, col = queue.pop(0)

                    # Update its distance
                    rooms[row][col] = dst

                    # Add its neighboring nodes to the queue.
                    for d_row, d_col in directions:
                        nei_row, nei_col = row + d_row, col + d_col

                        if (
                            0 <= nei_row < rows  # Check for a valid row.
                            and 0 <= nei_col < cols  # Check for a valid col.
                            and rooms[nei_row][nei_col]
                            > dst
                            + 1  # Check if the proposed distance is lesser than discovered distance.
                        ):
                            # Add valid neighbors to the queue.
                            queue.append([dst + 1, nei_row, nei_col])
        return rooms

