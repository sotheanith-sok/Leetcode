"""
Problem:
    Given an integer array nums, handle multiple queries of the following types:

    Update the value of an element in nums.
    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
    Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    void update(int index, int val) Updates the value of nums[index] to be val.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
    
    Example 1:
    Input
    ["NumArray", "sumRange", "update", "sumRange"]
    [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
    [null, 9, null, 8]
    Explanation
    NumArray numArray = new NumArray([1, 3, 5]);
    numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
    numArray.update(1, 2);   // nums = [1, 2, 5]
    numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Solution:
    Use a segement tree to solve this problem. The tree enables O(logn) times for calculating sum between a range and update a value. Each node in the segment tree contains two childrens, the start and end of a range of sum, and the total sum between those range. Recursively build the tree, update nodes, and calculate range sum.  

Complexity:
    Time: O(logn)
    Space: O(n)
"""

# The definition of segment node
class SegmentNode:
    def __init__(self, start, end):

        # The range of sum
        self.start, self.end = start, end

        # Pointers to the left and right child
        self.left, self.right = None, None

        # The total sum over those range
        self.val = 0


class NumArray:
    def __init__(self, nums: list[int]):
  
        # Recursively build a segment tree from a given list of numbers
        def createTree(l, r):

            # If the left and right pointers meet, this is the leaf of the tree 
            if l == r:
                n = SegmentNode(l, r)
                n.val = nums[l]
                return n

            # Else, calculate the mid pointer
            mid = (r - l) // 2 + l

            # Create a sigment node
            node = SegmentNode(l, r)

            # Recursively build the left child of this segment node
            node.left = createTree(l, mid)

            # Recursively build the right child of this segment node
            node.right = createTree(mid + 1, r)

            # Update the sum of this node with the sum of the left child and the sum of the right child
            node.val = node.left.val + node.right.val

            # Return the current node
            return node

        # Save nums such that we can quickly update nodes
        self.nums = nums

        # Build the segment tree
        self.root = createTree(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:

        # Calculate the difference that needed to be add all all nodes
        diff = val - self.nums[index]

        # Update the value in nums at index
        self.nums[index] = val

        # Recursively update all nodes
        def updateVal(node):

            # Add the difference to the current node
            node.val += diff

            # If there is a left child and the index fall between its range, recursively update the left child
            if node.left and node.left.start <= index <= node.left.end:
                updateVal(node.left)
            
            # Else if there is a right child and the index falls between its range, recursively update the right child
            elif node.right and node.right.start <= index <= node.right.end:
                updateVal(node.right)

        # Recursively update all nodes from the root
        updateVal(self.root)

    def sumRange(self, left: int, right: int) -> int:

        # Recursively calculate the sum over a given range
        def rangeSum(node, l, r):

            # If the range of the current node matches the left and right pointers, return the sum of this node
            if node.start == l and node.end == r:
                return node.val

            # Else, calculate the mid pointer
            mid = (node.end - node.start) // 2 + node.start

            # If the mid pointer falls between the left and right pointers, calculate the range sum by summing the partial sum from both children
            if l <= mid < r:
                return rangeSum(node.left, l, mid) + rangeSum(node.right, mid + 1, r)

            # If both pointers are less than the mid pointers, calculate the range sum from the left child
            if l <= r <= mid:
                return rangeSum(node.left, l, r)

            # Else, calculate the range sum from the right child
            return rangeSum(node.right, l, r)

        # Recursively calculate the range sum starting from the root
        return rangeSum(self.root, left, right)

