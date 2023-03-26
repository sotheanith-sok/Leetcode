"""
Problem:
    You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

    Return the length of the longest cycle in the graph. If no cycle exists, return -1.

    A cycle is a path that starts and ends at the same node.

    Example 1:
    Input: edges = [3,3,4,2,3]
    Output: 3
    Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
    The length of this cycle is 3, so 3 is returned.
    
    Example 2:
    Input: edges = [2,-1,3,1]
    Output: -1
    Explanation: There are no cycles in this graph.

Solution:
    Since there is at most one outgoing edge for each node, all nodes are belonging to at most one cycle. Iterate through all nodes. For each node, we will use it as the starting point and dfs through the graph to find the cycle. We found a cycle if we seen a node twice. Return the longest cycle.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def longestCycle(self, edges: list[int]) -> int:

        # Find the number of nodes
        n = len(edges)

        # Initialize the result and a dict to keep track of previously seen nodes
        res, seen = -1, {}

        # DFS through the graph to find a cycle
        def dfs(node, step):
            nonlocal res

            # If the current node has been seen previously, calculate the length of the cycle and update the result
            if node in seen:
                res = max(res, step - seen[node])

            # If the current node is the last node, end the search
            if edges[node] == -1:
                return

            # Else, save the next node and mark when we see the current node
            nextNode, seen[node] = edges[node], step

            # Mark the current node as visited by changing it to be the last node
            edges[node] = -1

            # Visit the next node
            dfs(nextNode, step + 1)

            # Unmark when we see the current node
            seen.pop(node)

        # Itereate through all nodes and find the longest cycle
        for node in range(n):
            dfs(node, 0)

        return res
