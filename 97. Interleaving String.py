""" 
Problem:
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

    An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
    Note: a + b is the concatenation of strings a and b.

    Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    
    Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
    
    Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true

Solution:
    We can rethink this problem into a graph problem. Form a adjacency matrix with character in s1 as the column and characters in s2 as the row. Move right means using a chracter from s2 and move down means using a chracter from s1. Then, we can perform BFS on the adjacency matrix and try to find the path from upper left (empty string) to lower right. Index of characters in s3 will be the BFS level. 

    Full Explanation: https://leetcode.com/problems/interleaving-string/discuss/31948/8ms-C%2B%2B-solution-using-BFS-with-explanation

Complexity:
    Time: O(m*n) 
    Space: O(m*n)
"""


from collections import deque


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # If the length of s1 + s2 is different than s3, we can't form s3 by interleaving s1 and s2 and thus, return False
        if len(s1) + len(s2) != len(s3):
            return False

        # BFS
        # Initalize a deque and add the starting node
        queue = deque([(-1, -1)])
        visit = set((-1, -1))

        # Determine which character in s3 to compare to
        k = 0

        # Iterate until queue is empty
        while queue:

            # Get how many nodes in this level
            i = len(queue)

            # Iterate thorugh all nodes
            for _ in range(i):

                # Pop a node
                c1, c2 = queue.popleft()

                # If we reach the lower right node, it means that we used all chracters from s1 and s2 and thus, it is possible to form an interleave. Don't worry about k since len(s3) == len(s1)+len(s2).
                if c1 == len(s1) - 1 and c2 == len(s2) - 1:
                    return True

                # Check if the down node can be visited
                if (
                    c1 + 1 < len(s1)
                    and (c1 + 1, c2) not in visit
                    and s1[c1 + 1] == s3[k]
                ):
                    queue.append((c1 + 1, c2))
                    visit.add((c1 + 1, c2))

                # Check if the right node can be visited
                if (
                    c2 + 1 < len(s2)
                    and (c1, c2 + 1) not in visit
                    and s2[c2 + 1] == s3[k]
                ):
                    queue.append((c1, c2 + 1))
                    visit.add((c1, c2 + 1))

            # Move to the next character
            k += 1

        return False

