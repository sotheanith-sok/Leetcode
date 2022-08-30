"""
Problem:
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

    Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
    
    Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Solution:
    Rotate matrix one layer at a time. Use a left and a right pointers to keep track of the starting and ending indices of a layer. Iterate until the left pointer meets the right pointer. For each iteration, go through all numbers using an offset i (aka iterate until left+i==right) and perform a 4 ways swap where

        top-left, top-right, bottom-right, bottom-left = bottom-left, top-left, top-right, bottom-right

    Below is how you access all above values from the matrix
        top-left = matrix[l][l+i]
        top-right = matrxi[l+i][r]
        bottom-right = matrix[r][r-i]
        bottom-left = matrxi[r-i][l]

Complexity:
    Time: O(n**2)
    Space: O(1)
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Find the dimesion of the matrix
        n = len(matrix)

        # Initialzie the left and right pointers
        l, r = 0, n - 1

        # Iterate until the left and right pointers meet
        while l < r:

            # Initialze the offset
            i = 0

            # While left + offset is less than right
            while l + i < r:

                # Perform the 4-ways swap
                # top-left, top-right, bottom-right, bottom-left = bottom-left, top-left, top-right, bottom-right
                (
                    matrix[l][l + i],
                    matrix[l + i][r],
                    matrix[r][r - i],
                    matrix[r - i][l],
                ) = (
                    matrix[r - i][l],
                    matrix[l][l + i],
                    matrix[l + i][r],
                    matrix[r][r - i],
                )

                # Increment the offset
                i += 1

            # Update the left and right pointers
            l, r = l + 1, r - 1

