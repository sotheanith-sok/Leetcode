"""
Problem:
    Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    You must find a solution with a memory complexity better than O(n2).

    Example 1:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
    
    Example 2:
    Input: matrix = [[-5]], k = 1
    Output: -5

Solution:
    Use binary search to solve this problem. We will search through the range of possible the solution. Initialize the left pointer to the min of the matrix and the right pointer to the max of the matrix. At each iteration, calculate the mid value and check how many values in the matrix is less than or equal to such value. If the count is larger than k, save this mid value as the possible solution and continue to search the left side. Else, search the right side.  

    This approach works because the last detected value will always guarantee be a value in the matrix since its has to have at least k elements smaller than it.    

    We can efficiently count the number of values less a number by iterating through every row from the right and check for the first element that is less than such a number. Then, add the count of remaining elements to the total count and go to the next row.   

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:

        # Find the number of rows and columns
        m, n = len(matrix), len(matrix[0])

        # A helper to function to find how many values in matrix less than value
        def countLessThanOrEqual(num):

            # Initialize the count to 0
            cnt = 0

            # Initialize the remaining coloumn to n
            j = n

            # Iterate through all rows
            for i in range(m):

                # Iterate until the remaining coloumn reach 0 or value at such (row, coloumn) is less than or equal to num
                while j > 0 and matrix[i][j - 1] > num:
                    j -= 1

                # Update the previous row ended coloumn and add remaining coloumns to count
                cnt = cnt + j

            return cnt

        # Initialize the left and right pointers to the min and max value of matrix
        l, r = matrix[0][0], matrix[m - 1][n - 1]

        # Initialize the result to 0
        res = 0

        # Iterate until the left and right pointer crossed
        while l <= r:

            # Find the mid value
            mid = (r - l) // 2 + l

            # If the count of elements less than or equal to mid value is larger than or equal to k,
            if countLessThanOrEqual(mid) >= k:

                # Save the mid value as the result
                res = mid

                # Continue to search the left side
                r = mid - 1

            # Else, continue to search the right side
            else:
                l = mid + 1

        return res

