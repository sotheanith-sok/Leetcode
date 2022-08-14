"""
Problem:
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

    Example 1:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    Explanation: There are 2 shortest transformation sequences:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
    "hit" -> "hot" -> "lot" -> "log" -> "cog"
    
    Example 2:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: []
    Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Solution:
    The initial instinct is to used BFS to find shortest paths and keep generating partial paths as we go from one level to another. However, this approach would cause TLE because we end up creating and destroying a lot of paths. Thus, we will avoid this problem by performing these three steps:

    1.  Adjacency List: We start by generating adjacency list mapped pattern to words. This approach is better than replacing each character in a word with every lower case alphabets because we avoid doing checking all 26 alphabet for every character. 

    i.e.    wordList = ["hot","dot","dog","lot","log","cog"]
            adj = {
                '*ot': ['hot', 'dot', 'lot'], 
                'h*t': ['hot'], 
                'ho*': ['hot'], 
                'd*t': ['dot'], 
                'do*': ['dot', 'dog'], 
                '*og': ['dog', 'log', 'cog'], 
                'd*g': ['dog'], 
                'l*t': ['lot'], 
                'lo*': ['lot', 'log'], 
                'l*g': ['log'], 
                'c*g': ['cog'], 
                'co*': ['cog']
            }

    2. BFS: Using the adjacency list generated in the previous step, we will traverse such list using BFS from beginWord to endWord and built a reversed adjacency list. The reversed adjacency list will map a word to all words that leading to it. 

    In order to account for all paths leading to a word while preventing adding duplicate next word to the queue, we will use two sets: Visited and VisitedCurrentLevel. 
    
    Visited set will be used to keep track of all words used in previous levels. Current words that isn't in such set will be added to the reversed adjacency list. 
    
    Next, the VisitedCurrentLevel will be used to keep track of all words used in the current level. A next word will only be added to a queue if it doesn't exist in such set. 
    
    After processing each level, we will merge the VisitedCurrentLevel set into the Visited set.

    i.e.    reversedAdj = {
                'hot': ['hit'], 
                'dot': ['hot'], 
                'lot': ['hot'], 
                'dog': ['dot'], 
                'log': ['lot'], 
                'cog': ['dog', 'log']
            }

    3. DFS: Use dfs to traverse the reversed adjacency list from endWord to beginWord and use a single queue to maintain constructed path. We add a next word to the front of the queue before we recursively go to such word and remove such word from the front of queue as we return. Once, the first word is equal to the beginWord, we have succesfully constructed a path. 

    i.e.    res = [
                ['hit', 'hot', 'dot', 'dog', 'cog'], 
                ['hit', 'hot', 'lot', 'log', 'cog']
            ]

Complexity:
    Time:
        1. AdjacencyList: O(nw) where n is length of wordList and w is the length of each word
        2. BFS: O(n)
        3. DFS: O(n)
    Space:
        1. AdjacencyList: O(nw) where n is length of wordList and w is the length of each word
        2. BFS: O(n)
        3. DFS: O(n)
"""


from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:

        # 1. Create adjacency list
        def adjacencyList():

            # Initialize the adjacency list
            adj = defaultdict(list)

            # Iterate through all words
            for word in wordList:

                # Iterate through all characters in a word
                for i, _ in enumerate(word):

                    # Create the pattern
                    pattern = word[:i] + "*" + word[i + 1 :]

                    # Add a word into the adjacency list based on its pattern
                    adj[pattern].append(word)

            return adj

        # 2. Create reversed adjacency list
        def bfs(adj):

            # Initialize the reversed adjacency list
            reversedAdj = defaultdict(list)

            # Initialize the queue
            queue = deque([beginWord])

            # Initialize a set to keep track of used words at previous level
            visited = set([beginWord])

            while queue:

                # Initialize a set to keep track of used words at the current level
                visitedCurrentLevel = set()

                # Get the number of words at this level
                n = len(queue)

                # Iterate through all words
                for _ in range(n):

                    # Pop a word from the front of the queue
                    word = queue.popleft()

                    # Generate pattern based on the current word
                    for i, _ in enumerate(word):

                        pattern = word[:i] + "*" + word[i + 1 :]

                        # Itereate through all next words
                        for nextWord in adj[pattern]:

                            # If the next word hasn't been used in previous levels
                            if nextWord not in visited:

                                # Add such word to the reversed adjacency list
                                reversedAdj[nextWord].append(word)

                                # If the next word hasn't been used in the current level
                                if nextWord not in visitedCurrentLevel:

                                    # Add such word to the queue
                                    queue.append(nextWord)

                                    # Mark such word as visited
                                    visitedCurrentLevel.add(nextWord)

                # Once we done with a level, add all words visited at this level to the visited set
                visited.update(visitedCurrentLevel)

                # If we visited the endWord, end the search
                if endWord in visited:
                    break

            return reversedAdj

        # 3. Construct paths based on the reversed adjacency list using DFS
        def dfs(reversedAdj, res, path):

            # If the first word in a path is beginWord, we have succesfully constructed a path
            if path[0] == beginWord:

                # Add such path to the result
                res.append(list(path))

                return

            # Else, get the first word in a path
            word = path[0]

            # Find next words using the reversed adjacency list
            for nextWord in reversedAdj[word]:

                # Add such next word to the path
                path.appendleft(nextWord)

                # Recursively go to the next word
                dfs(reversedAdj, res, path)

                # Remove such next word from the path
                path.popleft()

            # Return the result
            return res

        # Do all three steps
        adj = adjacencyList()
        reversedAdj = bfs(adj)
        res = dfs(reversedAdj, [], deque([endWord]))

        return res
