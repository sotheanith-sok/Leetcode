""" 
Problem:
    Given an m x n board of characters and a list of strings words, return all words on the board.

    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

    Example 1:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
    
    Example 2:
    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []

Solution:
    Instead of searching for each word by peforming dfs on each character, we will use a Trie or Prefix Tree to solve this problem. A trie is tree contains linked nodes where each node is a character and form chains that represent words. This data structure enables us to efficiently searching for words that have the same prefix. To start with, we will iterate through the board until we find the character that is a children of the root node. Then, we start our DFS through the tree from there until we reach a node that has been marked as the end of a word. Then, we append the word to the result. Continue until we reach a deadend and backtrack. For each iteration, a next node is determine by unvisited neighboring characters given in the board. 
    
    Note: We can reduce the number of the node to search through in a trie by removing any visited node that doesn't have any children aka all of its children have been visited.  

Complexity:
    Time: m n 4**(m n)
    Space: O(m n)
"""

# The trie node
class TrieNode:
    def __init__(self) -> None:

        # A hashmap mapping char -> trie node
        self.children = {}

        # Mark the end of a word
        self.isWord = False

    def add(self, word):

        # Start with root aka itself
        node = self

        # For each char in a word
        for char in word:

            # If it isn't in the hashamp
            if char not in node.children:

                # Add it
                node.children[char] = TrieNode()

            # Set the current node to that child
            node = node.children[char]

        # Lastly, mark this node as the end of the word
        node.isWord = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        # Create a trie tree
        root = TrieNode()

        # Add all words to the trie tree
        for word in words:
            root.add(word)

        # Create sets to store res and visited nodes
        res, visit = set(), set()

        # A helper function for directional movement
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # DFS to search through the trie tree
        def dfs(row, col, word, node, parentNode=None):

            # End the search if
            #   A given row and col aren't valid or
            #   This row and col already visited or
            #   The character at the given row and col isn't a child of the current node.
            if (
                row < 0
                or row >= ROWS
                or col < 0
                or col >= COLS
                or (row, col) in visit
                or board[row][col] not in node.children
            ):
                return

            # Save the current node a parent node
            parentNode = node

            # Update the current node to the child node.
            node = node.children[board[row][col]]

            # Append the character to the word
            word += board[row][col]

            # If the current node is the end of a word
            if node.isWord:

                # Add the word to the result
                res.add(word)

            # Mark the current row and col as visited
            visit.add((row, col))

            # DFS call on its neighbors
            for dRow, dCol in direction:
                neiRow, neiCol = row + dRow, col + dCol

                dfs(
                    neiRow, neiCol, word, node, parentNode,
                )

            # Mark the current row and col as unvisited
            visit.remove((row, col))

            # Remove the current node if it doesn't have any children as we already visited it
            # This will reduce the number of nodes in the trie tree
            if parentNode and len(node.children) == 0:
                parentNode.children.pop(board[row][col])

        # Get the rows and cols
        ROWS, COLS = len(board), len(board[0])

        # Perform DFS on all characters in the board
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, "", root)

        return list(res)

