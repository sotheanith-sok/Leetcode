"""
Problem:
    n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

    Take their own seat if it is still available, and
    Pick other seats randomly when they find their seat occupied
    Return the probability that the nth person gets his own seat.

    Example 1:
    Input: n = 1
    Output: 1.00000
    Explanation: The first person can only get the first seat.
    
    Example 2:
    Input: n = 2
    Output: 0.50000
    Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).

Solution:
    Let P be the probability that a person n-th get his seat. Thus, we can define P as

    P(n) =  1/n +                   # Probability of 1st person picked first sit                                             
            1/n * 0 +               # Probability of 1st person picked nth sit and nth person picked nth sit
            (n-2)/n * (             # Probability of 1st person picked 2nd to n-1 sit
                1/(n-2) * P(n-1) +      # Probability of 1st person picked 2nd sit and nth person pick nth sit given that there is only n-1 remaining sit
                1/(n-2) * P(n-2) +      # Probability of 1st person picked 3rd sit and nth person pick nth sit given that there is only n-2 remaining sit
                1/(n-2) * P(n-3) +      # Probability of 1st person picked 4th sit and nth person pick nth sit given that there is only n-3 remaining sit
                ... +
                1/(n-2) * P(3) +        # Probability of 1st person picked n-2 sit nd sit and nth person pick nth sit given that there is only 3 remaining sit
                1/(n-2) * P(2))         # Probability of 1st person picked n-1 sit nd sit and nth person pick nth sit given that there is only 2 remaining sit


    We can simplfy P to
    P(n) = 1/n + 1/n * (P(n-1) + P(n-2) + ... + P(2))

    Since P(1) == 1
    P(n) = 1/n * (P(n-1) + P(n-2) + ... + P(2) + P(1))

    If n>2: 
    n * P(n) =  P(n-1) + P(n-2) + ... + P(2) + P(1)
    (n+1) * P(n+1) = P(n) + P(n-1) + ... + P(3) + P(2) + P(1)

    subtract both equation

    n * P(n) - (n+1) * P(n+1) = -P(n)
    (n+1) * P(n) = (n+1) * P(n+1)
    P(n) = P(n+1)

    Thus, since P(2) = 0.5, any subsequent P(n>2) = 0.5

Complexity:
    Time: O(1)
    Space: O(1)
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:

        # P(1) = 1 and P(n>=2) = 0.5. Look up solution for mathematical proof
        return 1 if n == 1 else 0.5

