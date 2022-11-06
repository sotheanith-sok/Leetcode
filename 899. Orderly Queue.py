""" 
Problem:
    You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

    Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

    Example 1:
    Input: s = "cba", k = 1
    Output: "acb"
    Explanation: 
    In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
    In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
    
    Example 2:
    Input: s = "baaca", k = 3
    Output: "aaabc"
    Explanation: 
    In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
    In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".

Solution:
    There are only two possible options given k
    1. If k == 1, we can only rotate s based each index
        Ex: s = '1234' 
            nextWord = '2341', '3412', '4123', '1234'

    2. If k == 2, we can generate all possible combination of characters in s
        Ex: s = '1234', k = 2 
        nextWord without duplication
        ['1234'], 
        ['2341', '1342'], 
        ['3412', '2413', '3421', '1423'], 
        ['4123', '3124', '4132', '2134', '4213', '3214', '4231'], 
        ['1243', '3241', '1324', '4321', '2143', '3142', '2314', '4312'], ['2431', '1432']

    Thus, we return sorted(s) if k >= 2 or lexicographically minimum among all rotation if k == 1 
        
Complexity:
    Time: O(n**2)
    Space:O(n)
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return (
            "".join(sorted(s)) if k != 1 else min(s[i:] + s[:i] for i in range(len(s)))
        )
