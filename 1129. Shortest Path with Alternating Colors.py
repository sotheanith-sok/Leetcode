"""
Problem:
    You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

    You are given two arrays redEdges and blueEdges where:

    redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
    blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
    Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

    
    Example 1:
    Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
    Output: [0,1,-1]
    
    Example 2:
    Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
    Output: [0,1,-1]

Solution:
    Start by building adjacency lists for both red and blue edges. Then, BFS through the graph and find shortest path to reach all nodes. For each node, we can visit its neighboring nodes as long as the path to reach the current node is a different color than the path to reach such neighboring node and thus, there are two ways to visit all nodes. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:

        # Build adjacency lists for red and blue edges
        redAdj, blueAdj = defaultdict(list), defaultdict(list)

        for node1, node2 in redEdges:
            redAdj[node1].append(node2)

        for node1, node2 in blueEdges:
            blueAdj[node1].append(node2)

        # Initialize the result
        res = [-1] * n

        # Initialize a queue and a set to keep track of visited nodes and what edge color used to visit such node
        queue, visited = deque([(0, 0), (1, 0)]), set([(0, 0), (1, 0)])

        # Initialize the number of step
        step = 0

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes visitable at this step
            k = len(queue)

            # Process all nodes
            for _ in range(k):

                # Pop a node and the color of edge used to visit such node
                color, node = queue.popleft()

                # Update the result
                res[node] = step if res[node] == -1 else min(res[node], step)

                # Calculate the color of the next edge
                nextColor = abs(color - 1)

                # Add all neighboring nodes that haven't been visited yet into the queue and mark them as visited
                for nextNode in blueAdj[node] if nextColor == 1 else redAdj[node]:

                    if (nextColor, nextNode) in visited:
                        continue

                    visited.add((nextColor, nextNode))
                    queue.append((nextColor, nextNode))

            # Increment the step
            step += 1

        return res
