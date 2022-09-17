"""
Problem:
    Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

    Example 1:
    Input: words = ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
    
    Example 2:
    Input: words = ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]
    
    Example 3:
    Input: words = ["a",""]
    Output: [[0,1],[1,0]]

Solution:
    Use a trie tree to solve this problem. Add all words into the trie tree. Then, check for palindrome of the reverse of all words. Words in trie will be the i-th word and reversed words will be the j-th word. 

    A trie node store pointers to next trie node, the i-th word that end at such node, and all i-th words that ended at such node children. 

    To search for a palindrome in the trie tree, we will traverse the tree using each character of the j-th word. At every node, if there is a word that end at such node, it is a potential an i-th word. If we are able use up all characters of the j-th word, all future i-th words that ended at children of the last node are potentially an i-th word (Case: i = "aabbaa", j = "bbaa").

    The number of node traversed will represent the comparison that took place and we can use such number with two pointers to compare an i-th and a j-th words for palindrome without repeated work in linear time. 

    Optimization:
    1. Index based trie tree
    2. Palindrome checking between two words without repeated work and without string concatenation
    3. Use list instead of set for the trie node (Set is about 80% slower than list for looping and it will cause TLE) 

Complexity:
    Time: O(mn**2) where is m is the number of words and n is the length of the longest word
    Space: O(mn)
"""

from collections import defaultdict


class TrieNode:
    def __init__(self, words=None):

        # A list of words used for a quick look up since the trie node will work mostly with indices.
        self.words = words

        # Dictionary mapped this node to its child nodes
        self.children = defaultdict(TrieNode)

        # A list of i-th words ended at child nodes of the current node
        self.nextWords = []

        # The i-th word that ended at the current node
        self.word = -1

    # Add an i-th word into the trie tree
    def add(self, i):

        # Intialize the current node
        node = self

        # Use characters in the i-th word to traverse the trie tree
        for c in self.words[i]:

            # Append the i-th word into the list of words ended at child nodes of the current node
            node.nextWords.append(i)

            # Go to the next node
            node = node.children[c]

        # Save the i-th word at the last node
        node.word = i

    # Find all i-th word that make a palindrome with a given j-th word
    def find(self, j):

        # A variable to check if we are able to match all characters of the j-th word with characters in the trie tree
        matched = True

        # A list of potential i-th words
        candidates = []

        # Initialize the current node
        node = self

        # A variable to keep track of the number of comparison that have already been taken place between characters in the trie tree and the j-th word
        k = 0

        # Traverse the trie tree based on the reverse of the j-th word
        for c in reversed(self.words[j]):

            # If there is a word that end at the current node, add such word as a potential i-th word
            if node.word != -1 and node.word != j:
                candidates.append((k, node.word))

            # If there is a mismatch between characters in the trie tree and the j-th word, end the search
            if c not in node.children:
                matched = False
                break

            # Else, go to the next node
            node = node.children[c]

            # Increment the number of comparison
            k += 1

        # If we are able to match all characters in the j-th word with characters in the trie tree
        if matched:

            # If there is a word ended at the last node, it is potentially an i-th word
            if node.word != -1 and node.word != j:
                candidates.append((k, node.word))

            # All words ended at child nodes of the last node are also potentially i-th words
            for i in node.nextWords:
                if i == j:
                    continue
                candidates.append((k, i))

        # Testing all i-th words to see which one is a palindrome of the j-th word
        res = []

        # Iterate through all candidates
        for k, i in candidates:

            # If the current i-th word is a palindrome of the j-th word
            if self.isPalindrome(k, i, j):

                # Append both words into the result
                res.append([i, j])

        return res

    # Check if two words are a palindrome given we made kth comparison already
    def isPalindrome(self, k, i, j):

        # Find lengths of both words
        m, n = len(self.words[i]), len(self.words[j])

        # Intialize the left and right pointers
        l, r = k, m + n - 1 - k

        # while the left and right pointers haven't cross
        while l < r:

            # Find characters at both pointers
            c1, c2 = (
                self.words[i][l] if 0 <= l < m else self.words[j][l - m],
                self.words[i][r] if 0 <= r < m else self.words[j][r - m],
            )

            # If both characters are different, return False
            if c1 != c2:
                return False

            # Else, increment the left pointer and decrement the right pointer
            l, r = l + 1, r - 1

        # Return true if all characters matched
        return True


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:

        # Find the number of words
        n = len(words)

        # Initialize the trie tree
        trie = TrieNode(words)

        # Add i-th words into the trie tree
        for i in range(n):
            trie.add(i)

        # Initialize the result
        res = []

        # Find pairs of word giving j-th word
        for j in range(n):
            res += trie.find(j)

        return res

