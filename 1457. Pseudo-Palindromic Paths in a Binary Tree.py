"""
Problem:
    Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

    Example 1:
    Input: root = [2,3,1,3,1,null,1]
    Output: 2 
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
    
    Example 2:
    Input: root = [2,1,1,1,3,null,null,null,null,null,1]
    Output: 1 
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
    
    Example 3:
    Input: root = [9]
    Output: 1

Solution:
    DFS through the tree. Keep counts of all digits that we discovered. When we reach a leaf node, check if the counter can form a palindrome. A counter of digits can form a palindrom if there is at most a digit with an odd count. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        # Check if a counter can form a palindrom
        def isPalindrome(counts):
            return sum(count % 2 != 0 for count in counts.values()) < 2

        # Initialize the counter
        counts = defaultdict(int)

        # DFS through the tree
        def dfs(node):

            # If there is no node, return 0
            if not node:
                return 0

            # Intialize a variable to keep track of the number of palindromes
            palindrome = 0

            # Add the current character to the counter
            counts[node.val] += 1

            # If the current node has a child, check for palindrome in its left and right child
            if node.left or node.right:
                palindrome = dfs(node.left) + dfs(node.right)

            # Else, we have reached a leaf node, return if a counter of digits leading up to such node can form a palindrome
            else:
                palindrome = int(isPalindrome(counts))

            # Remove the current character from the counter
            counts[node.val] -= 1

            # Return the number of palindromes
            return palindrome

        return dfs(root)

