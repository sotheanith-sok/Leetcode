"""
Problem:
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or equal to 2 * 109.

    Example 1:
    Input: m = 3, n = 7
    Output: 28
    
    Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

Solution:
    Just like any dynamic programming problems, it is harder to figure out the formula behind the solution than actually coding the solution. So, we will start by finding answers to some m and n. Below is the generated array of answers. 

        mn  1   2   3   4   5   6   7
        1   1   1   1   1   1   1   1
        2   1   2   3   4   5   6   7
        3   1   3   6   10  15  21  28
        4   1   4   10  20  35  56  84
        5   1   5   15  35  70  126 210

    As we can see, uniquePaths(m,n) == uniquePaths(m-1,n) + uniquePaths(m,n-1) where m == 1 or n == 1 is the base case and we return 1. The intuition behind this is that to to find uniquePaths(3,3) we have to figure it out how many paths lead into (3,3) aka uniquePaths(3,2) + uniquePaths(2,3) since we can only move down or right.  

Complexity:
    Time: O(mn)
    Space: O(mn)
"""

from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @lru_cache(None)
        def paths(i, j):

            # If we reach 1st row or column, return 1 as it is our basecase
            if i == 1 or j == 1:
                return 1

            # Else, return the numbers of unique paths lead to its previous nodes. 
            return paths(i - 1, j) + paths(i, j - 1)

        return paths(m, n)
