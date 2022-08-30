"""
Problem:
    Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

    For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

    Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

    We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

    Example 1:
    Input: strs = ["tars","rats","arts","star"]
    Output: 2
    
    Example 2:
    Input: strs = ["omv","ovm"]
    Output: 1

Solution:
    Use disjoint set to store all words. Then, for each word, check if there is another word that is similar to it. If yes, merge them in the disjoint set. Lastly, return numbers to set in the disjoint set. 

Complexity:
    Time: O(mn**3) where m is the length of the longest words and n is the numbers of words

          O(n**2): pairing all words
          O(m): check if two words are similar
          O(n): union two words

    Space: O(n)
"""


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:

        # Definition of the disjoint set
        class Disjoint:

            # Constructor
            def __init__(self, n) -> None:

                # Initialize a list to store parents of each node based on indices
                self.parents = list(range(n))

                # The number of remaining disjoint set in the disjoint set
                self.size = n

            # Given a node, recursively find its root node
            def find(self, i):
                return self.find(self.parents[i]) if self.parents[i] != i else i

            # Union two nodes
            def union(self, i, j):

                # Find the root of both nodes
                rootI, rootJ = self.find(i), self.find(j)

                # If both nodes belong to a different set, merge them
                if rootI != rootJ:

                    # Make the root of i node as a child of the root of j node
                    self.parents[rootI] = rootJ

                    # Decrement the number of remaining disjoint set
                    self.size -= 1

        # Compare two words
        def similar(word1, word2):

            # Initialize the number of different between both words
            diff = 0

            # Check all character pairs
            for c1, c2 in zip(word1, word2):

                # If both characters are different, increment the different
                if c1 != c2:
                    diff += 1

                # If there are more than 2 characters different, return False
                if diff > 2:
                    return False

            # Else, return True
            return True

        # Find the number of words
        n = len(strs)

        # Initialize the disjoint set
        dis = Disjoint(n)

        # Pair up all words
        for i in range(n):
            for j in range(i + 1, n):

                # If both words are similar
                if similar(strs[i], strs[j]):

                    # Union them in the disjoint set
                    dis.union(i, j)

        return dis.size

