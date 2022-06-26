""" 
Problem:
    You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.

    The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

    Return the minimum cost it takes to connect the two groups.

    Example 1:
    Input: cost = [[15, 96], [36, 2]]
    Output: 17
    Explanation: The optimal way of connecting the groups is:
    1--A
    2--B
    This results in a total cost of 17.
    
    Example 2:
    Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
    Output: 4
    Explanation: The optimal way of connecting the groups is:
    1--A
    2--B
    2--C
    3--A
    This results in a total cost of 4.
    Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
    
    Example 3:
    Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
    Output: 10

Solution:
    This isn't a optimal solution but it is way easier to implement than the Hungarian Maximum Matching Algorithm. We will use DFS to pair nodes in graph 1 with all nodes in graph 2. Iterate through all nodes in graph 1. At each iteration, calculate the cost if we connect such node to all nodes in graph 2. We will use a bitmap to keep track of which nodes in graph 2 hasn't been much yet. The base case is when we iterated through all nodes in graph 1 and there is still node in graph 2 that hasn't been mapped to yet. At this point, we will just be greedy and pick the minimum edges for all unmatch nodes in graph 2. As we iterate through nodes, we can cache the cost of remaining unmatch nodes if we matched x amount of nodes from graph 1. Use nodes from graph 1 and bitmap as the key.   

Complexity:
    Time: O(mn 2**m
    Space: O(n 2**m)
"""


from math import inf


class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:

        # Get the number of nodes from graph 1 and graph 2.
        m, n = len(cost), len(cost[0])

        # Calculate the mincost for nodes in graph 2 if we were to connect it to all nodes in graph 1
        minN = [min(cost[i][j] for i in range(m)) for j in range(n)]

        # Cache used to store cost mapped the the number of nodes picked from graph 1 and the number of nodes still unmatch from graph 2 (aka the bitmap)
        cache = {}

        # DFS
        def dfs(i, mask):

            # Return the cost if we cached already
            if (i, mask) in cache:
                return cache[(i, mask)]

            # Assume res is inf if we havn't reach the base case. Else, 0
            res = inf if i < m else 0

            # DFS through all nodes
            if i < m:

                # Find the minimum cost if we match this node from graph 1 with all nodes from graph 2.
                for j in range(n):
                    res = min(res, cost[i][j] + dfs(i + 1, mask | 1 << j))

            # We reach base case after we iterate through all nodes in graph 1
            else:

                # Find all unmatch nodes using bitmaps and greedily match them to nodes in graph 1.
                for j in range(n):
                    if mask & 1 << j == 0:
                        res += minN[j]

            # Cache the result once we calculated it.
            cache[(i, mask)] = res

            return res

        return dfs(0, 0)

