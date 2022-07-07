""" 
Problem:
    Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

    Recall that:

    The node of a binary tree is a leaf if and only if it has no children
    The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
 

    Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation: We return the node with value 2, colored in yellow in the diagram.
    The nodes coloured in blue are the deepest leaf-nodes of the tree.
    Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
    
    Example 2:
    Input: root = [1]
    Output: [1]
    Explanation: The root is the deepest node in the tree, and it's the lca of itself.
    
    Example 3:
    Input: root = [0,1,3,null,2]
    Output: [2]
    Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.

Solution:
    Use DFS to recursively traverse the tree. Then, for every node, it will return the maximum depth of its two subtrees. If a node has the depth of its left subtree equal to its right subtree, it is a common ancestor of some leaf nodes. Thus, we will save the node based on its depth into the hashmap. It is okay to overide the node since the last node of a depth will be the common of all leaf nodes at such depth. 

Complexity:
    Time: O(n)
    Space: O(h)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        # Map leaf depth with common ancestors
        hashmap = {}

        # Perform DFS
        def dfs(node, level):

            # If we reach a none node, return previous level
            if not node:
                return level - 1

            # Calcualte the depth of the left subtree 
            maxLevelLeft = dfs(node.left, level + 1)

            # Calculate the depth of the right subtree
            maxLevelRight = dfs(node.right, level + 1)

            # If both subtrees are equal in depth, this node is a common ancestor
            if maxLevelLeft == maxLevelRight:

                # Save the current node into the hashmap
                hashmap[maxLevelLeft] = node

            # Return the max depth of subtrees
            return max(maxLevelLeft, maxLevelRight)

        return hashmap[dfs(root, 0)]

