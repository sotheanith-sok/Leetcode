"""
Problem:
    A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

    Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

    For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
    There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

    Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

    Note that the starting point is assumed to be valid, so it might not be included in the bank.

    Example 1:
    Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
    Output: 1
    
    Example 2:
    Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
    
    Example 3:
    Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    Output: 3

Solution:
    Build an adjacency list so we that we know next genes given a gene. Then, we can use BFS to search until we found a path from starting gene to the ending gene. If there isn't a path, return -1 

Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""


from collections import defaultdict, deque
from itertools import product


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:

        # Check if it is even possible to reach the end gene
        if end not in bank:
            return -1

        # Check if gene1 can be converted to gene2 by using exactly 1 move
        def isValid(gene1, gene2):
            diff = 0
            for c1, c2 in zip(gene1, gene2):
                diff += int(c1 != c2)
                if diff == 2:
                    return False
            return True

        # Add the starting gene isn't the bank
        bank.append(start)

        # Build adjacency list
        adj = defaultdict(list)
        for gene1, gene2 in product(bank, repeat=2):

            # If gene1 is the same as gene2, skip it
            if gene1 == gene2:
                continue

            # Check if we can move from gene1 to gene2
            if isValid(gene1, gene2):
                adj[gene1].append(gene2)

        # Start BFS
        # Initialize the queue and a visited set
        queue, visited = deque([start]), set([start])

        # Initialize the current step
        step = 0

        # Iterate until the queue is empty
        while queue:

            # Find how many genes at this step
            k = len(queue)

            # Process all genes
            for _ in range(k):

                # Pop a gene
                gene = queue.popleft()

                # If the current gene is equal to the ending gene, return the step
                if gene == end:
                    return step

                # Add next genes that we haven't visited yet into the queue
                for nextGene in adj[gene]:
                    if nextGene not in visited:
                        queue.append(nextGene)
                        visited.add(nextGene)

            # Increment the step count
            step += 1

        return -1

