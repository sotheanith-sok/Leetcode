"""
Problem:
    There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

    You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

    Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.


    Example 1:
    Input: n = 4, connections = [[0,1],[0,2],[1,2]]
    Output: 1
    Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
    
    Example 2:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    Output: 2
    
    Example 3:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
    Output: -1
    Explanation: There are not enough cables.

Solution:
    Use a disjoint set to represent clusters of computers. Iterate through all connections and union each pair of computers together. If two computers already exist in the same cluster when we try to union them, we have found a free connection. Finally, return the number of connections required to connect all clusters together if we have enough connections. Else, return -1. 

Complexity:
    Time: O(n log h) where n is the number of connections and h is the height of the disjoint tree. 
    Space: O(n)
"""


class Disjoint:
    def __init__(self, n):

        # Initialize an array of keep track of parents of each nodes
        self.parents = [-1] * n

        # Initialize an array to keep track of the depths of each trees
        self.depths = [1] * n

    def find(self, node):
        # Recursively find the root node of each tree

        # If we have reach a root node, return it
        if self.parents[node] == -1:
            return node

        # Else, keep going up
        return self.find(self.parents[node])

    def union(self, node1, node2):

        # Find the root node of both nodes
        root1, root2 = self.find(node1), self.find(node2)

        # If both nodes belong to the same tree, return False
        if root1 == root2:
            return False

        # Else, ensuring the first tree is deeper than the second tree
        if self.depths[root1] < self.depths[root2]:
            root1, root2 = root2, root1

        # Make the second tree a child of the first tree
        self.parents[root2] = root1

        # Update the depth of the first tree
        self.depths[root1] += int(self.depths[root1] == self.depths[root2])

        return True


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:

        # Initialize two variables to keep track of numbers of free connections and clusters
        freeConnections, clusters = 0, n

        # Initailize the disjoint set
        dis = Disjoint(n)

        # Iterate through all connections
        for node1, node2 in connections:

            # If both computers belong to a different cluster, union them and reduce the number of cluster
            if dis.union(node1, node2):
                clusters -= 1

            # Else, we have found a free
            else:
                freeConnections += 1

        # If we have enough connections to connect all remaining clusters return such number
        # Else, return -1
        return clusters - 1 if clusters - 1 <= freeConnections else -1
