""" 
Problem:
    Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

    However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

    Return the least number of units of times that the CPU will take to finish all the given tasks.

    Example 1:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: 
    A -> B -> idle -> A -> B -> idle -> A -> B
    There is at least 2 units of time between any two same tasks.
    
    Example 2:
    Input: tasks = ["A","A","A","B","B","B"], n = 0
    Output: 6
    Explanation: On this case any permutation of size 6 would work since n = 0.
    ["A","A","A","B","B","B"]
    ["A","B","A","B","A","B"]
    ["B","B","B","A","A","A"]
    ...
    And so on.
    
    Example 3:
    Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    Output: 16
    Explanation: 
    One possible solution is
    A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Solution:
    Since we don't have to return the actual tasks, we don't have to keep track of it. We will use a heap to keep track of the count of each task and a queue to keep track of tasks that have been timeout. Repeat the process until heap and queue are empty. At each time, check if a task on top of a queue can be use again. If yes, pop it from the queue and add it to the heap. If a heap isn't empty, we pop a task and decrement its count. Then, append such task with expected available time into the queue. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        # Add counts of tasks into a heap
        heap = [-v for v in Counter(tasks).values()]
        heapq.heapify(heap)

        # Initialize a queue to keep track of timeout tasks.
        queue = deque()
        time = 0

        # Repeat until heap and queue are empty
        while heap or queue:

            # Increment the time.
            time += 1

            # If there is a task on top of a queue is available at this time, add it to the heap.
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

            # If the heap isn't empty, pop a task from it and decrement its count.
            if heap:
                count = heapq.heappop(heap) + 1

                # If the count hasn't reach 0, append the task to the queue.
                if count < 0:
                    queue.append((count, time + n + 1))

        return time

