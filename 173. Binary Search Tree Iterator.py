""" 
Problem:
    Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    int next() Moves the pointer to the right, then returns the number at the pointer.
    Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

    You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

    Example 1:
    
    Input
    ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    Output
    [null, 3, 7, true, 9, true, 15, true, 20, false]

    Explanation
    BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
    bSTIterator.next();    // return 3
    bSTIterator.next();    // return 7
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 9
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 15
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 20
    bSTIterator.hasNext(); // return False


Solution:
    We will use iterative version of DFS to solve this problem. Just like recursive dfs, we will create a stack to store unvisited nodes. The order by which we are adding nodes into the stack is based on the binary tree. This means that for any given node, we will add the node itself and its left child (if existed) onto the stack. Then we add the left child of its left child onto to the stack too. The process is repeated until there isn't anymore left child. Then, when we call the next() function, we simply pop the node on top of the stack and then add that node's right child and subsequence left child onto the stack. To check if there is a next node, we simply check if there exisits a node in the stack.    

Complexity:
    Time: O(1) average
    Space: O(h) where h is the height of the tree. 

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):

        # DFS stack.
        self.stack = []

        # Set current node to the root.
        node = root

        # Add node and its subsequence left children onto the stack.
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:

        # Pop the resulting node from the stack.
        res = self.stack.pop()

        # Get the node right child.
        node = res.right

        # If the right child exists, add it and its subsequence left children onto the stack.
        while node:
            self.stack.append(node)
            node = node.left

        return res.val

    def hasNext(self) -> bool:

        # Check if the stack is empty
        return len(self.stack) != 0
