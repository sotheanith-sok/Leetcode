"""
Problem:
    You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

    You are also given a string s of length n, where s[i] is the character assigned to node i.

    Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

    Example 1:
    Input: parent = [-1,0,0,1,1,2], s = "abacbe"
    Output: 3
    Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
    It can be proven that there is no longer path that satisfies the conditions. 
    
    Example 2:
    Input: parent = [-1,0,0,0], s = "aabc"
    Output: 3
    Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.

Solution:
    For a given node, the path can be divided into two partitions: left and right. 
    
    If the longest path consisted of such node and its subtree only, both partitions are the longest path from such node to one of its child node. 
    
    Else, the longest path must be consisted of another node that is not part of the current subtree and a partition of the current subtree is a part of a larger partition of a larger subtree.

    Start by building an adjacency list and dfs through the tree starting from 0 node. For each node, calculate the longest path consists of such node and its subtree only. Then, return the largest partition to its parent node.    

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:

        # Find the number of nodes
        n = len(parent)

        # Build an adjacency list
        adj = defaultdict(list)
        for node in range(n):
            adj[parent[node]].append(node)

        # Initialize the result
        res = 0

        # Find the longest path starting from a given node to one of its child
        def dfs(node):

            nonlocal res

            # Intialize the length of the left and right partitions
            left, right = 0, 0

            # Visit next nodes
            for nextNode in adj[node]:

                # Calculate the longest path starting from the current and pass through the next node
                path = dfs(nextNode)

                # If the next node has the same label as the current node, skip such node
                if s[node] == s[nextNode]:
                    continue

                # Else, update the left and right partitions to store the two longest paths
                right = max(right, path)
                left, right = max(left, right), min(left, right)

            # Update the result
            res = max(res, 1 + left + right)

            # Return the longest path starting from a given node to one of its child
            return 1 + left

        dfs(0)

        return res
