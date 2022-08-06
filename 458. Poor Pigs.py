"""
Problem:
    There are buckets buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

    You can feed the pigs according to these steps:

    Choose some live pigs to feed.
    For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time.
    Wait for minutesToDie minutes. You may not feed any other pigs during this time.
    After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
    Repeat this process until you run out of time.
    Given buckets, minutesToDie, and minutesToTest, return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.

    Example 1:
    Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
    Output: 5

    Example 2:
    Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
    Output: 2

    Example 3:
    Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
    Output: 2

Solution:
    To solve this problem, we need to figure out the maximum amount of buckets solvable given a fixed amount of tests and pigs used. The amount of test can be calculated as the floor(minutesToTest/minutesToDie).

    Given: minutesToTest == 60, minutesToDie == 15, test == floor(60/15) == 4
    Let pigs == 1. We can arrange buckets as a following:
    
    1   2   3   4   5

    As we can see, with 1 pig, we can solve at most 5 buckets in 4 tests because if the pig doesn't die from the first 4 buckets, we know that the last bucket contains the poison.

    Let pigs == 2. We can arrange buckets as the following:

    1   2   3   4   5
    6   7   8   9   10 
    11  12  13  14  15
    16  17  18  19  20
    21  22  23  24  25

    Follow the same approach as pigs == 1, we will feed one pig each row per test and another pig each coloumn per test. This approach will let us know which row and column contains the poison. 

    From examples above, we can see that the maximum amount of buckets solvable is equal to the number of test + 1 and raise to the number of pigs used.
        bucketsSolvable == (test+1)^pigs

    Thus, to solve this problem, we have to find the number of pigs used such that the maximum amount of buckets solvable is larger than or equal to the number of buckets.


Complexity:
    Time: O(log n (buckets))
    Space: O(1)
"""


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

        # Initialize the number of pig used to 0
        pigs = 0

        # Calculate the number of test
        test = minutesToTest // minutesToDie

        # Calculate the maximum amount of buckets solvable
        bucketsSolvable = (test + 1) ** pigs

        # While the maximum amount of buckets solvable is less than the buckets
        while bucketsSolvable < buckets:

            # Increment the number of pig used
            pigs += 1

            # Recalculate the maximum amount of buckets solvable
            bucketsSolvable = (test + 1) ** pigs

        return pigs
