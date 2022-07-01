""" 
Problem:
    You are given an integer array arr.

    We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

    Return the largest number of chunks we can make to sort the array.

    Example 1:
    Input: arr = [5,4,3,2,1]
    Output: 1
    Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
    
    Example 2:
    Input: arr = [2,1,3,4,4]
    Output: 4
    Explanation:
    We can split into two chunks, such as [2, 1], [3, 4, 4].
    However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

Solution:
    We will start by assuming each number is its own chunk and we will keep track of the minimum and maximum number in such chunk. Iterate through all numbers. At each iteration, if the minimum number of the current chunk is less than the maximum number of the previous chunk, we pop the previous chunk from the stack and merge it with the current chunk. Repeat until the stack is empty or the condition is no longer true. Lastly, add the current chunk to the stack and continue to the next chunk. Finally, the size of the stack will be the answer. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:

        # Initialize the stack to keep track of previous chunk
        stack = []

        # Add the first number as its own chunk to the stack
        stack.append((arr[0], arr[0]))

        for i in range(1, len(arr)):

            # Create a chunk from the number at i
            minNum, maxNum = arr[i], arr[i]

            # Merge the current chunk with previous chunks if the maximum number of previous chunk is larger than the minimum number of the current chunk
            while stack and stack[-1][1] > minNum:
                prevMinNum, prevMaxNum = stack.pop()
                minNum, maxNum = min(prevMinNum, minNum), max(prevMaxNum, maxNum)

            # Add the current chunk to the stack
            stack.append((minNum, maxNum))

        return len(stack)

