"""
Problem:
    You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

    Return the number of pairs of different nodes that are unreachable from each other.

    Example 1:
    Input: n = 3, edges = [[0,1],[0,2],[1,2]]
    Output: 0
    Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
    
    Example 2:
    Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    Output: 14
    Explanation: There are 14 pairs of nodes that are unreachable from each other:
    [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
    Therefore, we return 14.

Solution:
   Divide all nodes into clusters and pairs all nodes in a cluster with all nodes outside of such cluster. Return the sum of all pairs.

   Ex: Let there be 5 clusters of size [a, b, c, d ,e]

   1st cluster pairs count = a*b + a*c + a*d + a*e = a * (b + c + d + e) 
   2nd cluster pairs count = b*c + b*d + b*e = b * (c + d + e)
   3rd cluster pairs count = c*d + c*e = c * (d + e)
   4th cluster pairs count = d*e
   5th cluster pairs count = 0

Complexity:
    Time: O(V + E) where V is the number of nodes and E is the number of edges
    Space: O(V)
"""

from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:

        # Build an adjacency list
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # DFS through the graph and count the number of nodes
        visited = set()

        def dfs(node):

            # If the current node already visited, return 0
            if node in visited:
                return 0

            # Else, mark the current node as visited
            visited.add(node)

            # Return the number of nodes starting from the current node
            return 1 + sum(dfs(j) for j in adj[node] if j not in visited)

        # Initialize the result
        res = 0

        # Iterate through all nodes
        for node in range(n):

            # If the current node belong to a previous cluster, skip it
            if node in visited:
                continue

            # Else, count the number of nodes in the current cluster
            count = dfs(node)

            # Find the number of nodes outside the current cluster
            n -= count

            # Increment the result with the number of pairs
            res += count * n

        return res
