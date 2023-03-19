"""
Problem:
    Design a data structure that supports adding new words and finding if a string matches any previously added string.

    Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
    
    Example:
    Input
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
    [null,null,null,null,false,true,true,true]

    Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True

Solution:
    Use a trie to represent words in the dictionary. Then, we can dfs through the trie tree to search for a word based on its character where a dot is treated as a wildcard.  

Complexity:
    Time: O(log(25))
    Space: O(n) where n is the combination of all characters and positions
"""

from collections import defaultdict


class Trie:
    def __init__(self):

        # Initialize a dict to link this node to its children nodes
        self.children = defaultdict(lambda: Trie())

        # Initialize a boolean flag to mark an end of a word
        self.isWord = False

    def add(self, word):

        # Initialize the current node
        node = self

        # Add new nodes based on each character of a given word
        for c in word:
            node = node.children[c]

        # Mark the last node as the end of a word
        node.isWord = True

    def search(self, word):

        # Find the length of a word
        n = len(word)

        # DFS through the trie tree to find if a word existed
        def dfs(i, node):

            # If we have reach the end of a word, return the result based on the boolean flag
            if i == n:
                return node.isWord

            # Else, visit next node if the next character existed
            #   or 
            #       visit all next node is the next character is a wild card
            
            if (
                word[i] in node.children and dfs(i + 1, node.children[word[i]])
                ) or (
                word[i] == "." and any(dfs(i + 1, node.children[c]) for c in node.children)
            ):
                # End the search early if we have found the word
                return True

            return False

        return dfs(0, self)


class WordDictionary:
    def __init__(self):

        # Initialize the trie tree
        self.trie = Trie()

    def addWord(self, word: str) -> None:

        # Add all words into the trie tree
        self.trie.add(word)

    def search(self, word: str) -> bool:

        # Search the trie tree
        return self.trie.search(word)
