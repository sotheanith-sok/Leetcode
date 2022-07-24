"""
Problem:
    Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    

    Example 1:
    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
    Output: true
    
    Example 2:
    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
    Output: false

Solution:
    Use binary search to solve this problem. Since we are working with a 2-d array, there are 3 regions to search for when the the target is less than the mid value and 3 regions to search for the target is larger than mid value.

    ie given an array:
    [
        [ 1,   2,   3,   4,   5],
        [ 6,   7,   8,   9,  10],
        [11,  12,  13,  14,  15],
        [16,  17,  18,  19,  20],
        [21,  22,  23,  24,  25]
    ]

    If target is less than mid, you have search in these 3 regions.

    1. Bottom-Left
    [[11,  12],
     [16,  17],
     [21,  22]]

    2. Top-Left
    [[ 1,   2],
     [ 6,   7]]

    3. Top-Right
    [[ 3,   4,   5],
     [ 8,   9,  10]]

    If target is greater than mid, you have search in these 3 regions.

    1. Bottom-Left
    [[16,  17,  18],
     [21,  22,  23]]

    2. Bottom-Right
    [[19,   20],
     [24,   25]]

    3. Top-Right
    [[ 4,   5],
     [ 9,  10],
     [14,  15]]

Complexity:
    Time: O(logn)
    Space: O(1)
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def binary(rStart, rEnd, cStart, cEnd):

            # If the row or column pointers crossed or went out of bound, return False
            if not (
                0 <= rStart <= rEnd < len(matrix)
                and 0 <= cStart <= cEnd < len(matrix[0])
            ):
                return False

            # Find the mid pointers of a given array
            rMid, cMid = (
                ((rEnd - rStart) // 2) + rStart,
                ((cEnd - cStart) // 2) + cStart,
            )

            # If target is equal to the mid value, return True
            if target == matrix[rMid][cMid]:
                return True

            # If target is less than the mid value, search the bottom-left, top-left, top-right regions
            elif target < matrix[rMid][cMid]:
                if (
                    binary(rMid, rEnd, cStart, cMid - 1) # Bottom-left
                    or binary(rStart, rMid - 1, cMid, cEnd) # Top-right
                    or binary(rStart, rMid - 1, cStart, cMid - 1) # Top-left
                ):
                    return True
            # Else, if the target is greater than the mid value, search bottom-left, bottom-right, top-right regions
            else:
                if (
                    binary(rMid + 1, rEnd, cStart, cMid) # Bottom-left
                    or binary(rStart, rMid, cMid + 1, cEnd) # Bottom-right
                    or binary(rMid + 1, rEnd, cMid + 1, cEnd) # Top-Right
                ):
                    return True

            return False

        return binary(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

