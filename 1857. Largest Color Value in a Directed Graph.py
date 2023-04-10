"""
Problem:
    There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

    You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

    A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

    Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

    
    Example 1:
    Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
    Output: 3
    Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
    
    Example 2:
    Input: colors = "a", edges = [[0,0]]
    Output: -1
    Explanation: There is a cycle from 0 to 0.

Solution:
    Use topological sort to solve this problem. Start by building an adjacency list and a list of in-degrees of all nodes. For each no in-degree nodes, find the largest color values such node can contribute to its neighboring nodes.
    A node can contribute to the color values of its neighboring nodes if it has a color with a higher value than what previous node contributed. Then, remove such node from the graph by reducing all in-degree of neighboring nodes by 1. Lastly, add any neighboring nodes with no in-degree and repeat. Return the largest color value.

    A graph does not contain a cycle if we process all nodes as we perform a topological sort.

Complexity:
    Time: O(26n)
    Space: O(26n)
"""

from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:

        # Find the number of nodes
        n = len(colors)

        # Intialize the adjacency list and the list of in-degree
        adj, degrees = defaultdict(list), [0] * n

        # Iterate through all edges
        for node1, node2 in edges:

            # Update the adjacency list
            adj[node1].append(node2)

            # Update the in-degree list
            degrees[node2] += 1

        # Add all nodes with 0 in-degree into the queue
        queue = deque(node for node, degree in enumerate(degrees) if not degree)

        # Initialize the result and color values of all nodes (for all colors)
        res, colorValues = 0, defaultdict(lambda: defaultdict(int))

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes at this level
            k = len(queue)

            # Process all nodes
            for _ in range(k):

                # Pop a node from the queue
                node = queue.popleft()

                # Update such node color values include its color
                colorValues[node][colors[node]] += 1

                # Since this node has no in-degree, its color values contain the highest values of all paths
                # Update the result with the higest color value found
                res = max(res, max(colorValues[node].values()))

                # Reduce the number of unprocessed node by 1
                n -= 1

                # Iterate through all nodes
                for nextNode in adj[node]:

                    # Check if the current node color values can contribute to its nieghboring nodes color values
                    for color in colorValues[node]:
                        colorValues[nextNode][color] = max(
                            colorValues[node][color], colorValues[nextNode][color]
                        )

                    # Reduce neighboring nodes in-degree by 1
                    degrees[nextNode] -= 1

                    # Add all new 0 in-degree nodes into the queue
                    if not degrees[nextNode]:
                        queue.append(nextNode)

        # Return the result if there is no cycle
        # Else, return -1
        return res if n == 0 else -1
