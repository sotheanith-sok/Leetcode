""" 
Problem:
    You are given two strings of the same length s1 and s2 and a string baseStr.

    We say s1[i] and s2[i] are equivalent characters.

    For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
    Equivalent characters follow the usual rules of any equivalence relation:

    Reflexivity: 'a' == 'a'.
    Symmetry: 'a' == 'b' implies 'b' == 'a'.
    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
    For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

    Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

    Example 1:
    Input: s1 = "parker", s2 = "morris", baseStr = "parser"
    Output: "makkek"
    Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
    The characters in each group are equivalent and sorted in lexicographical order.
    So the answer is "makkek".
    
    Example 2:
    Input: s1 = "hello", s2 = "world", baseStr = "hold"
    Output: "hdld"
    Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
    So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
    
    Example 3:
    Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
    Output: "aauaaaaada"
    Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".

Solution:
    Use a disjoint set to represent groups of equivalent characters. Two trees must be merged such that the lexicographically smallest character always be the root.

    Then, iterate through all chracters in both strings and union pairs of characters into the disjoint set. Next, iterate through the base string and convert each character to the character at the root of its tree.  

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import defaultdict


class Disjoint:
    def __init__(self) -> None:

        # Initialize a dict to keep track of parents of all nodes
        self.parents = defaultdict(lambda: -1)

    def find(self, c):
        # Recursively find the root node for a given character

        # If we reach a root node, return the character
        if self.parents[c] == -1:
            return c

        # Else, keep going up
        return self.find(self.parents[c])

    def union(self, c1, c2):
        # Union two characters together by merging their respective tree

        # Find the root nodes of both nodes
        p1, p2 = self.find(c1), self.find(c2)

        # If both characters belong to the same tree, we don't have to do anything
        if p1 == p2:
            return

        # Else, merge both trees such that the lexicographically smallest character always be the root
        self.parents[p1], self.parents[p2] = (-1, p1) if p2 > p1 else (p2, -1)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        # Initialize the disjoint set
        dis = Disjoint()

        # Union pairs of character into the set
        for c1, c2 in zip(s1, s2):
            dis.union(c1, c2)

        # Convert each character to the character at the root of its tree
        return "".join([dis.find(c) for c in baseStr])
