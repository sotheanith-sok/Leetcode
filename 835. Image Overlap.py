""" 
Problem:
    You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

    We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

    Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

    Return the largest possible overlap.

    Example 1:
    Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
    Output: 3
    Explanation: We translate img1 to right by 1 unit and down by 1 unit.
    The number of positions that have a 1 in both images is 3 (shown in red).

    Example 2:
    Input: img1 = [[1]], img2 = [[1]]
    Output: 1
    
    Example 3:
    Input: img1 = [[0]], img2 = [[0]]
    Output: 0

Solution:
    Just bruteforce the solution. Get all 1s position of img1 and img2. Then, for each pair of point from both images, calculate their difference in rows and cols and store how many time we see each difference. Return the largest count of the difference as the solution.  

Complexity: 
    Time: O(n**4)
    Space: O(n**2)
"""


from collections import defaultdict
from itertools import product


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:

        # Find the dimension of the image
        n = len(img1)

        # Find all 1s positions of both images
        img1, img2 = (
            [
                (row, col)
                for row, col in product(range(n), repeat=2)
                if img1[row][col] == 1
            ],
            [
                (row, col)
                for row, col in product(range(n), repeat=2)
                if img2[row][col] == 1
            ],
        )

        # Initialize a dict to store counts of the difference of rows and cols
        counts = defaultdict(int)

        # Iterate through all pairs
        for (sRow, sCol), (tRow, tCol) in product(img1, img2):

            # Increment the count of the difference by 1
            counts[(tRow - sRow, tCol - sCol)] += 1

        return max(counts.values()) if counts else 0

