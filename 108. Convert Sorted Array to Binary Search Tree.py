"""
Problem:
    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

    Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

    Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Solution:
    Partition nums in the middle where the mid number will form a node and the left and right partitions will form its respective subtrees of such node. Continue to divide each partition until they are empty. Finally, return constructed  nodes from each recursive call. 

Complexity:
    Time: O(n)
    Space: O(1)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:

        # Recursively build the binary tree
        def build(start, end):

            # If both pointers are valid, construct the node represent the partition
            if 0 <= start <= end < len(nums):

                # Find the mid pointer
                mid = (end - start) // 2 + start

                # Build the node contains the number at the mid pointer and points to child nodes constructed from its left and right partitions
                node = TreeNode(nums[mid], build(start, mid - 1), build(mid + 1, end))

                # Return built node
                return node

            # If there isn't a partition to build a node from, return None
            return None

        return build(0, len(nums) - 1)
