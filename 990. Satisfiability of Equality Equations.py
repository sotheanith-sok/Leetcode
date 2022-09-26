"""
Problem:
    You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

    Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

    Example 1:
    Input: equations = ["a==b","b!=a"]
    Output: false
    Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
    There is no way to assign the variables to satisfy both equations.
    
    Example 2:
    Input: equations = ["b==a","a==b"]
    Output: true
    Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Solution:
    Use UnionFind to solve this problem. Iterate through all equations and union all characters that is equal to each other. Then, iterate through all equation again and try to find two characters that isn't equal but was union together. Return False if we found one. Else, return True

Complexity:
    Time: O(n)
    Space: O(1)
"""

from collections import defaultdict


# Defintion of the UnionFind
class UnionFind:
    def __init__(self) -> None:

        # Intialize a dict to keep track of parents of all nodes. -1 if a node doesn't a parent.
        self.parents = defaultdict(lambda: -1)

    # Recursively find the parent of a given node
    def find(self, node):

        # If the current node does not have a parent, return such node
        if self.parents[node] == -1:
            return node

        # Else, find the parent of the parent of the current node
        return self.find(self.parents[node])

    # Union two nodes together
    def union(self, node1, node2):

        # Find parents of node1 and node2
        p1, p2 = self.find(node1), self.find(node2)

        # If their parents are different, union them together
        if p1 != p2:
            self.parents[p1] = p2


class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:

        # Initialzie the UnionFind
        uf = UnionFind()

        # Union all characters that are equal to each other
        for equation in equations:
            if equation[1:-1] == "!=":
                continue

            uf.union(equation[0], equation[-1])

        # Try to find two characters that are not equal but was union together
        return not any(
            uf.find(equation[0]) == uf.find(equation[-1])
            for equation in equations
            if equation[1:-1] == "!="
        )

