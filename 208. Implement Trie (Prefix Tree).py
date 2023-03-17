"""
Problem:
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
    
    Example 1:
    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]
    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True

Solution:
    Build a trie tree composed of nodes that represent characters. Each node contains a link to subsequence nodes and a boolean flag to mark the end of a word. Perform iterative DFS for the word and prefix search.  

Complexity:
    Time: O(k) where k is the length of the longest word
    Space: O(n) where n is the combination of unique characters and their position in their respective words 
"""


from collections import defaultdict


class Trie:
    def __init__(self):

        # Initialize a dict that link the current trie node to subsequence node
        self.children = defaultdict(lambda: Trie())

        # Initialize a boolean flag to mark the end of a word
        self.isWord = False

    def insert(self, word: str) -> None:

        # Initialize the current node
        node = self

        # Iterate through the tree until we reach the last node
        for c in word:
            node = node.children[c]

        # Mark such node as an end of a word
        node.isWord = True

    def search(self, word: str) -> bool:

        # Initialize the current node
        node = self

        # Traverse the tree based on each character of a given word
        for c in word:

            # If there is no child node corresponding to the current character, return False
            if c not in node.children:
                return False

            # Else, continue to the next node
            node = node.children[c]

        # Return True if we found a word
        return node.isWord

    def startsWith(self, prefix: str) -> bool:

        # Initialize the current node
        node = self

        # Traverse the tree based on each character of a given word
        for c in prefix:

            # If there is no child node corresponding to the current character, return False
            if c not in node.children:
                return False

            # Else, continue to the next node
            node = node.children[c]

        return True
