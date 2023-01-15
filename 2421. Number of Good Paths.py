"""
Problem:
    There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

    You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

    A good path is a simple path that satisfies the following conditions:

    The starting node and the ending node have the same value.
    All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
    Return the number of distinct good paths.

    Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

    

    Example 1:
    Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
    Output: 6
    Explanation: There are 5 good paths consisting of a single node.
    There is 1 additional good path: 1 -> 0 -> 2 -> 4.
    (The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
    Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
    
    Example 2:
    Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
    Output: 7
    Explanation: There are 5 good paths consisting of a single node.
    There are 2 additional good paths: 0 -> 1 and 2 -> 3.
    
    Example 3:
    Input: vals = [1], edges = []
    Output: 1
    Explanation: The tree consists of only one node, so there is one good path.

Solution:
    Use a disjoint set to group all nodes that have the same values. In order to ensure that a pair of nodes will only be grouped where all in-between nodes are less or equal to the pair of nodes, we will work from nodes with smallest values first and utilize an adjacency list of nodes mapped to other nodes of lesser or equal values.

    Example: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]

    1. Build an adjacency list
        {1: [0], 2: [0, 3], 4: [2]}

    2. Group all nodes based on its value
        {1: [0, 3], 2: [2], 3: [1, 4]}

    3. Iterate from the smallest values. For each group of nodes, union them to their neighboring nodes and find the combination of nodes in the same tree in the disjoint set

    val     nodes       disjoint                        res
    _       _           [(0), (1), (2), (3), (4)]       5
    1       [0, 3]      [(0), (1), (2), (3), (4)]       5 + comb(1, 2) + comb(1, 2) = 5
    2       [2]         [(0, 2, 3), (1), (4)]           5 + comb(1, 2)
    3       [1, 4]      [(0, 1, 2, 3, 4)]               5 + comb(2, 2) = 6


Complexity:
    Time: O(n**3 logn)
    Space: O(n)
"""

from collections import defaultdict
from itertools import product
from math import comb


class Disjoint:
    def __init__(self, n) -> None:

        # Intialize lists to keep track of parent nodes and heights
        self.parents, self.heights = [-1] * n, [0] * n

    def find(self, node):
        # Find the parent node recursively

        if self.parents[node] == -1:
            return node

        return self.find(self.parents[node])

    def union(self, node1, node2):
        # Union two nodes together while keeping the tree hieght minimum

        # Find parent nodes of both nodes
        parent1, parent2 = self.find(node1), self.find(node2)

        # If both nodes belong to the same tree, return
        if parent1 == parent2:
            return

        # Else, make the first tree the shorter of the two
        if self.heights[parent1] > self.heights[parent2]:
            parent1, parent2 = parent2, parent1

        # Merge the first tree under the second tree
        self.parents[parent1] = parent2

        # Update the height of the second tree
        self.heights[parent2] += int(self.heights[parent1] == self.heights[parent2])


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:

        # Find the number of nodes
        n = len(vals)

        # Build an adjacency list
        adj = defaultdict(list)
        for node1, node2 in edges:
            if vals[node1] <= vals[node2]:
                adj[node2].append(node1)

            if vals[node1] >= vals[node2]:
                adj[node1].append(node2)

        # Group all nodes based on their values
        nodes = defaultdict(list)
        for i, val in enumerate(vals):
            nodes[val].append(i)

        # Initialize the result and the disjoint set
        res, dis = n, Disjoint(n)

        # Iterate through all groups of nodes sorted by their values
        for val in sorted(nodes):

            # For each node in a group
            for node in nodes[val]:

                # Union such node with its neighboring nodes
                for node1, node2 in product([node], adj[node]):
                    dis.union(node1, node2)

            # Find how many nodes of the current values belong to the same tree in the disjoint set
            groups = defaultdict(int)
            for node in nodes[val]:
                groups[dis.find(node)] += 1

            # Calculate the combination of nodes in each tree
            for count in groups.values():
                res += comb(count, 2)

        return res
