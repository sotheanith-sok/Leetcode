"""
Problem:
    You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

    You are also given two integers node1 and node2.

    Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

    Note that edges may contain cycles.

    Example 1:
    Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
    Output: 2
    Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
    The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

    Example 2:
    Input: edges = [1,2,-1], node1 = 0, node2 = 2
    Output: 2
    Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
    The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.

Solution:
    Since all nodes have only at most a single out going edge, a path, starting from some arbitrary node to all other nodes, will always be the shorest path. Start by calculating the distance between node1 and node2 and other nodes. Then, find a node that is reachable by node1 and node2 with the shortest max distance. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict
from math import inf


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:

        # DFS through the graph and find distances from the starting node to all other nodes
        def dfs(i, node, dst):

            # If we reaches a dead end or a visited node, return the collection of distances
            if node == -1 or node in dst:
                return dst

            # Else, store the distance to the current node
            dst[node] = i

            # Go to the next node
            return dfs(i + 1, edges[node], dst)

        # Calculate distances from node1 and node2 to other nodes
        dst1, dst2 = dfs(0, node1, defaultdict(lambda: inf)), dfs(
            0, node2, defaultdict(lambda: inf)
        )

        # Find the number of nodes
        n = len(edges)

        # Initialize the result and longest possible distance + 1
        res, minDst = -1, n

        # Iterate through all possible nodes reachable by node 1
        for node in dst1:

            # Calculate the maximum distance to reach such node from node1 and node2
            dst = max(dst1[node], dst2[node])

            # If the current maximum distance is equal to the previous maximum distance, update the result with a smaller node
            if dst == minDst:
                res = node if res == -1 else min(res, node)

            # If the current maximum distance is less than the previous maximum distance, update the result
            if dst < minDst:
                res, minDst = node, dst

        return res
