""" 
Problem:
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
    
    Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true
    
    Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false

Solution:
    Iterate through all cells of the board and use each cell as a starting position. Then, DFS from such position to see if we can find the target word. 

Complexity:
    Time: O((mn)**2)
    Space: O(mn)
"""


from collections import Counter
from itertools import chain, product


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        # Find lengths of rows, cols and words
        m, n, k = len(board), len(board[0]), len(word)

        # Check if there are enough characters on the board to form the target word
        if m * n < k:
            return False

        # Check if there are enough occurences of characters required to form the target word
        count1, count2 = Counter(chain.from_iterable(board)), Counter(word)
        if count2 - count1:
            return False

        # Start DFS
        # Initialize a set to store visited cells
        visited = set()

        # A helper function for 4 directional movement
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # DFS through the board trying to match ith character of the target word with a given cell
        def dfs(i, row, col):

            # If we reach the last character of the target word and such character is same as the character at the current cell, we have found the word
            if i == k - 1 and board[row][col] == word[i]:
                return True

            # If there is a mismatch between ith character and the current cell, end the search
            if board[row][col] != word[i]:
                return False

            # Else, continue to next cells
            for dRow, dCol in directions:

                nRow, nCol = row + dRow, col + dCol

                # Check if we can visit a given next cell
                if 0 <= nRow < m and 0 <= nCol < n and (nRow, nCol) not in visited:

                    # If yes, mark such cell as visited
                    visited.add((nRow, nCol))

                    # Try to visit such cell
                    # If we found the word, return True
                    if dfs(i + 1, nRow, nCol):
                        return True

                    # Else, unmark such cell as visited
                    visited.remove((nRow, nCol))

        # Iterate through all rows and cols
        for row, col in product(range(m), range(n)):

            # Mark the starting cell as visited
            visited.add((row, col))

            # If we found the word by starting at this cell, return True
            if dfs(0, row, col):
                return True

            # Else, unmark such cell as visited
            visited.remove((row, col))

        return False
