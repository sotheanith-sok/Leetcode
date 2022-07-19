"""
Problem:
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
    Example 2:
    Input: numRows = 1
    Output: [[1]]

Solution:
    If the number of rows is less than or equal to 2, we can just return the base case. Else, we will calculate each subsequent rows starting from 2 of the pascal triangle one at a time and append each row into the result. Each row starts and ends with 1 and all values in between are calculated from neighboring pairs of values from the previous row.   
    
Complexity:
    Time: O(n(n+1)/2) or O(n**2)
    Space: O(n**2)
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        # If the number of rows is less than or equal to 2, return the base case
        if numRows <= 2:
            return [[1]] if numRows == 1 else [[1], [1, 1]]

        # Initialize the result
        res = [[1], [1, 1]]

        # Calculate the 2nd row and so on
        for _ in range(2, numRows):

            # A row starts with 1
            row = [1]

            # Calculate the sum of neighboring pairs of values from the previous row
            for j in range(len(res[-1]) - 1):
                row.append(res[-1][j] + res[-1][j + 1])

            # A row end with 1
            row.append(1)

            # Append a row to the result
            res.append(row)

        return res
