""" 
Problem:
    Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

    The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

    
    Example 1:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
    Output: 8 
    Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
    
    Example 2:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
    Output: 6
    Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
    
    Example 3:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
    Output: 0

Solution:
    Start by building an adjacency list from given edges. Then, we will dfs through the tree while keeping track of the previous node to prevent cycling. 
    
    For each node, we will calculate the time requires to reach all nodes that have an apple in its subtree. Then, we will add 2 to account for time required to reach such node from its parent node unless it is a root node. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:

        # Initialize the adjacency list
        adj = defaultdict(list)

        # Iterate through all edges and add them to the adjacency list
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # DFS through the tree and find the total time requires to reach all nodes that have an apple
        def dfs(pNode, node):

            # If there is a single next node and it is the same as the previous node, we have reach a leaf node
            # Thus, return 2 if such leaf node has an apple else 0.
            if len(adj[node]) == 1 and adj[node][0] == pNode:
                return 2 * int(hasApple[node])

            # If the current node is not a leaf node, sum up all times required to reach all nodes that contain an apple of each subtree
            res = sum(
                dfs(node, nextNode) for nextNode in adj[node] if nextNode != pNode
            )

            # If the current node is a root node, return the total time
            if node == 0:
                return res

            # Else, add 2 to the total time if there is at least a single node in the current subtree that has an apple
            return res + 2 if res > 0 or hasApple[node] else 0

        return dfs(-1, 0)
