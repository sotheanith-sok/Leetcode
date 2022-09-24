"""
Problem:
    A super ugly number is a positive integer whose prime factors are in the array primes.

    Given an integer n and an array of integers primes, return the nth super ugly number.

    The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

    Example 1:
    Input: n = 12, primes = [2,7,13,19]
    Output: 32
    Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].
    
    Example 2:
    Input: n = 1, primes = [2,3,5]
    Output: 1
    Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].

Solution:
    Ugly number is a number that composed of a multiple of given prime numbers. Thus, we start by initializing a heap with a value of 1. Then, to find an ugly number, we simply pop the smallest number from the heap. Next, we use the last ugly number and multiply it with each prime numbers and add those numbers into the heap. Repeat until we found n-th ugly number. 

    1. Avoid Duplication
    Since we take the last ugly number and multiply it with all prime numbers, there will be duplicated ugly numbers. ie given primes=[2, 7], duplicate ugly numbers are 1*2*7 and 1*7*2. Thus, we can avoid such duplication by saving the index of the prime number that was used to generate each ugly number. Then, we can calculate next ugly numbers by multiplying the current ugly number with prime numbers starting from such index.

    2. Heap Optimized
    We can optimize above solution further by avoiding populating heap with ugly numbers that we might not need. 

    For example: given primes = [2, 7, 13, 19] and n = 3
    ugly        heap
    [1]         [2, 7, 13, 19]
    [1, 2]      [4, 7, 13, 14, 19, 26, 38]
    [1, 2, 4]   [7, 8, 13, 14, 19, 26, 28, 38, 52, 76]

    We end up calculating future ugly numbers when a more recent one hasn't been picked yet. Ex: ugly[2] * 13 is calculated when ugly[0] * 13 isn't even picked yet.  

    To avoid above problem, we will keep track of a prime number and a previous ugly number used to generate each ugly number. When we pick an ugly number from the heap, we only have to calculate a single next ugly number by taking the prime number multiply by the current ugly number. 

    ugly        primes -> ugly                  heap
    [1]         {2:0, 7:0, 13:0, 19:0}          [2, 7, 13, 19]
    [1, 2]      {2:1, 7:0, 13:0, 19:0}          [4, 7, 13, 19]
    [1, 2, 4]   {2:2, 7:0, 13:0, 19:0}          [7, 8, 13, 19]

Complexity:
    Time: 
        1. O(nlog(k**n)) 
        2. O(nlogk)
    Space:  
        1. O(k**n)    
        2. O(k)
"""

import heapq

# Avoid Duplication Solution
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:

        # Find number of prime numbers
        k = len(primes)

        # Intialize the heap
        heap = [(1, 0)]

        # Intialize the result
        res = 0

        # Calculate n ugly numbers
        for _ in range(n):

            # Pop an ugly number and an index of the prime number used to generate such ugly number from the heap
            res, j = heapq.heappop(heap)

            # Calculate next ugly numbers starting from the above index
            for i in range(j, k):
                heapq.heappush(heap, (res * primes[i], i))

        return res


# Heap Optimized Solution
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:

        # Intialize the result
        res = [1]

        # Intialzie the heap storing (ugly number, prime, index of previous ugly number)
        heap = [(prime * res[0], prime, 0) for prime in primes]
        heapq.heapify(heap)

        # While we haven't found n ugly number yet
        while len(res) < n:

            # Pop an ugly number from the heap
            ugly, prime, i = heapq.heappop(heap)

            # Append such ugly number into the result if it isn't a duplicate
            if ugly != res[-1]:
                res.append(ugly)

            # Calcualte the next ugly number and append it onto the heap
            heapq.heappush(heap, (prime * res[i + 1], prime, i + 1))

        return res[-1]

