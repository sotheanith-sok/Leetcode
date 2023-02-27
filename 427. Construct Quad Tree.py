"""
Problem:
    Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

    Return the root of the Quad-Tree representing the grid.

    Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

    A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

    val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
    isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
    class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;
    }
    We can construct a Quad-Tree from a two-dimensional area using the following steps:

    If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
    If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
    Recurse for each of the children with the proper sub-grid.

    If you want to know more about the Quad-Tree, you can refer to the wiki.

    Quad-Tree format:

    The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

    It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

    If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

    Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
    Explanation: The explanation of this example is shown below:
    Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

    Example 2:
    Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
    Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
    The topLeft, bottomLeft and bottomRight each has the same value.
    The topRight have different values so we divide it into 4 sub-grids where each has the same value.
    Explanation is shown in the photo below:

Solution:
    Start by building a prefix sum so that we can find the sum of all values in any subgrid in constant time. Then, we will continue to divide the grid into 4 subgrids until each subgrid contains all zeros or ones. Return the root node.

Complexity:
    Time: O(n^2)
    Space: O(n^2)
"""


from collections import defaultdict
from itertools import product


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:

        # Find the length of rows and cols
        n = len(grid)

        # Initialize the prefix sum
        prefixSum = defaultdict(int)

        # Calculate the sum of all subgrid starting from the top left and ending at each cell
        for row, col in product(range(n), repeat=2):
            prefixSum[(row, col)] = (
                grid[row][col]
                + prefixSum[(row - 1, col)]
                + prefixSum[(row, col - 1)]
                - prefixSum[(row - 1, col - 1)]
            )

        # Recursively divide the grid into 4 subgrids until each subgrid contains all zeros and ones
        def divide(minRow, maxRow, minCol, maxCol):

            # Calculate the expected grid sum if such grid contains all zeroes and all ones
            zeros, ones = 0, (maxRow - minRow + 1) * (maxCol - minCol + 1)

            # Calculate the actual grid sum
            value = (
                prefixSum[(maxRow, maxCol)]
                - prefixSum[(maxRow, minCol - 1)]
                - prefixSum[(minRow - 1, maxCol)]
                + prefixSum[(minRow - 1, minCol - 1)]
            )

            # If a grid contains all zeros or all ones, we have reach a leaf node
            if value == zeros or value == ones:
                return Node(int(value == ones), True, None, None, None, None)

            # Else, calculate mid points to divide the grid into 4 subgrids
            midRow, midCol = (maxRow - minRow) // 2 + minRow, (
                maxCol - minCol
            ) // 2 + minCol

            # Divde the grid into 4 equal subgrids.
            return Node(
                -1,
                False,
                divide(minRow, midRow, minCol, midCol),
                divide(minRow, midRow, midCol + 1, maxCol),
                divide(midRow + 1, maxRow, minCol, midCol),
                divide(midRow + 1, maxRow, midCol + 1, maxCol),
            )

        return divide(0, n - 1, 0, n - 1)
