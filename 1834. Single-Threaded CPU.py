""" 
Problem:
    You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

    You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

    If the CPU is idle and there are no available tasks to process, the CPU remains idle.
    If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
    Once a task is started, the CPU will process the entire task without stopping.
    The CPU can finish a task then start a new one instantly.
    Return the order in which the CPU will process the tasks.

    Example 1:
    Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
    Output: [0,2,3,1]
    Explanation: The events go as follows: 
    - At time = 1, task 0 is available to process. Available tasks = {0}.
    - Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
    - At time = 2, task 1 is available to process. Available tasks = {1}.
    - At time = 3, task 2 is available to process. Available tasks = {1, 2}.
    - Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
    - At time = 4, task 3 is available to process. Available tasks = {1, 3}.
    - At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
    - At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
    - At time = 10, the CPU finishes task 1 and becomes idle.
    
    Example 2:
    Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    Output: [4,3,2,0,1]
    Explanation: The events go as follows:
    - At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
    - Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
    - At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
    - At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
    - At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
    - At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
    - At time = 40, the CPU finishes task 1 and becomes idle.

Solution:
    We will maintain two min heaps of "tasks" and "queuedTasks" where "tasks" contains all tasks that are not ready to process and "queuedTasks" contains all tasks that are ready to process. 
    Iterate until both heaps are empty. At each iteration, if there is a task that is ready process, add it to the "queuedTasks". Then, process all queued tasks and update the current time appropriately. Lastly, if we can't add any task to the "queuedTasks" and the "queuedTasks" is empty, update the current time to the enqueue time of the next recent task. 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:

        # Initialize the two min heaps of tasks and queuedTasks
        tasks, queuedTasks = [
            (enqueueTime, processingTime, i)
            for i, (enqueueTime, processingTime) in enumerate(tasks)
        ], []
        heapq.heapify(tasks)

        # Intiailize the current time and result
        time, res = 0, []

        # Iterate until both heaps are empty
        while tasks or queuedTasks:

            # Add all tasks that are ready into the queuedTasks
            if tasks and tasks[0][0] <= time:
                _, processingTime, i = heapq.heappop(tasks)
                heapq.heappush(queuedTasks, (processingTime, i))
                continue

            # If there is no task in the queuedTasks, update the current time to the enqueue time of the next recent task 
            if not queuedTasks:
                time = tasks[0][0]
                continue

            # Else, process a task in the queuedTasks and update the current time and result
            processingTime, i = heapq.heappop(queuedTasks)
            time += processingTime
            res.append(i)

        return res
