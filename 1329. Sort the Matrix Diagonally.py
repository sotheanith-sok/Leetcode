"""
Problem:
    A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

    Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

    Example 1:
    Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    
    Example 2:
    Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
    Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

Solution:
    Use heap to sort the matrix diagonally. Start by iterating through all values in the matrix and add such value along with the different between row and col into the heap. The different will ensure that all diagonal will be sorted together. We will also keep track of the starting row and col of each different. 

    Then, pop a different and a value from the heap. Use the different to find the corresponding row and col and add the value to such location. Lastly, increment the row and col corresponding to such different. Repeat until the heap is empty.  

Complexity:
    Time: O(nlogn) where n is all values in the matrix
    Space: O(n)
"""


import heapq
from itertools import product


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:

        # Get lengths of rows and cols
        m, n = len(mat), len(mat[0])

        # Intialize a dict to keep track of starting row and col for each different
        starts = {}

        # Intialize the heap to store differences and values
        heap = []

        # Iterate thorugh all values in the matrix
        for row, col in product(range(m), range(n)):

            # Calculate the different
            diff = row - col

            # If this is the first time we see such different
            if diff not in starts:

                # Add the row and col into the dict
                starts[diff] = (row, col)

            # Add different and value into the heap
            heap.append((diff, mat[row][col]))

        # Heapify the heap
        heapq.heapify(heap)

        # While heap isn't empty
        while heap:

            # Pop a different and a value
            diff, val = heapq.heappop(heap)

            # Find the corresponding row and col
            (row, col) = starts[diff]

            # Save the value at such row and col
            mat[row][col] = val

            # Update the row and col corresponded with such different
            starts[diff] = (row + 1, col + 1)

        return mat
