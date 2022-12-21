""" 
Problem:
    We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

    Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

    Example 1:
    Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: group1 [1,4] and group2 [2,3].
    
    Example 2:
    Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false
    
    Example 3:
    Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false

Solution:
    A group of nodes can be divided into at most two groups where each group contains no pair of nodes that are incompatible if we can traverse the graph to mark all nodes and there are no two adjacent nodes belonging to the same group.

    Start by building an adjacency list using the "dislikes" as edges. Then, visit all nodes using dfs and mark them as belonging to a group that is the opposite of its parent node. Continue to mark next node as long as it has not been marked yet. If we encounter a next node that has been marked and it belongs to the same group as the current node, we return False as there is no way to divide nodes into at most two groups.

Complexity:
    Time: O(V + E)
    Space: O(V + E)
"""


from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:

        # Build an adjacency list
        adj = defaultdict(list)
        for node1, node2 in dislikes:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # Initialize a dict to keep track of marked nodes and their corresponding groups
        marked = {}

        # DFS through all nodes and mark its group
        def dfs(node, group):

            # Mark the current node with its group
            marked[node] = group

            # Check all next nodes
            for nextNode in adj[node]:

                # If the next node is marked and its group is the same as the current group, return False
                if nextNode in marked and marked[nextNode] == marked[node]:
                    return False

                # If the next node is not marked and marking such node leads to two adjacency nodes belonging to the same group, return False
                if nextNode not in marked and not dfs(nextNode, not group):
                    return False

            # Return True if we can mark all nodes
            return True

        # Iterate through all nodes
        for node in adj:

            # If the current node is marked, skip it
            if node in marked:
                continue

            # Else, try to mark it
            # Return false if marking such node leads to two adjacency nodes belonging to the same group
            if not dfs(node, True):
                return False

        # Return True if we can mark all nodes
        return True
