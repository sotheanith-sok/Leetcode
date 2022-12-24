""" 
Problem:
    There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

    You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

    Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

    Example 1:
    Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Output: [8,12,6,10,10,10]
    Explanation: The tree is shown above.
    We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
    equals 1 + 1 + 2 + 2 + 2 = 8.
    Hence, answer[0] = 8, and so on.
    
    Example 2:
    Input: n = 1, edges = []
    Output: [0]
    
    Example 3:
    Input: n = 2, edges = [[1,0]]
    Output: [1,1]

Solution:
    For any arbitrary node, we can find the sum of edges connected to its child node by partition all nodes into two part: nodes that are one step futher from a child node and nodes that are one step closer to such child node. Then, we can find the sum of edges connected to the child node using the following formula

    sum of edges connected to a child node = 
                                        sum of edges connected to the parent node - 
                                        number of nodes in the child subtree + 
                                        number of nodes not in the child subtree

    Thus, we can solve this problem in 3 steps
    1. Build an adjacency list from all edges
    2. DFS through the tree and calculate the sum of edges connected to a root node and the number of nodes in all subtrees.
    3. DFS through the tree again starting from the root node and calculate the sum of edges connected to each node. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:

        # 1. Build an adjacency list
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # Initialize two lists: numbers of nodes in each subtree and sum of edges connected to each node
        nodes, edges = [1] * n, [0] * n

        # DFS through the tree and calculate numbers of nodes in each subtree and the sum of edges connected to a root node
        def dfs1(node, prevNode):

            # Iterate through next nodes
            for nextNode in adj[node]:

                # If the next node is the same as the parent node, skip it
                if nextNode == prevNode:
                    continue

                # Else, keep going down
                dfs1(nextNode, node)

                # Calculate the number of nodes in this subtree
                nodes[node] += nodes[nextNode]

                # Calculate the sum of edges for this subtree only
                edges[node] += nodes[nextNode] + edges[nextNode]

        # DFS through the tree again starting from the root node and calculate the sum of edges connected to each node
        def dfs2(node, prevNode):

            # Iterate through all nodes
            for nextNode in adj[node]:

                # If the next node is the same as the parent node, skip it
                if nextNode == prevNode:
                    continue

                # Calculate the sum of edges connected to this node
                edges[nextNode] = edges[node] - nodes[nextNode] + (n - nodes[nextNode])

                # Go to the next node
                dfs2(nextNode, node)

        dfs1(0, -1)
        dfs2(0, -1)
        return edges
