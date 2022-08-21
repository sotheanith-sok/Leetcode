"""
Problem:
    You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

    In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

    For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
    place stamp at index 0 of s to obtain "abc??",
    place stamp at index 1 of s to obtain "?abc?", or
    place stamp at index 2 of s to obtain "??abc".
    Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
    We want to convert s to target using at most 10 * target.length turns.

    Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

    Example 1:
    Input: stamp = "abc", target = "ababc"
    Output: [0,2]
    Explanation: Initially s = "?????".
    - Place stamp at index 0 to get "abc??".
    - Place stamp at index 2 to get "ababc".
    [1,0,2] would also be accepted as an answer, as well as some other answers.
    
    Example 2:
    Input: stamp = "abca", target = "aabcaca"
    Output: [3,0,1]
    Explanation: Initially s = "???????".
    - Place stamp at index 3 to get "???abca".
    - Place stamp at index 0 to get "abcabca".
    - Place stamp at index 1 to get "aabcaca".

Solution:
    Start from the last placement, find a substring of target that is equal to stamp. If there is one, add its starting index to the result and replace all values at such indices with a wildcard. We use a wildcard because it doesn't matter what characters at that position anymore since we will override it with the placement of a stamp later on and thus, any wildcard will match with any character in stamp. Repeat until there isn't any substring that can match the stamp. If we replaced all characters of the target, we found a solution and thus, return result. Else, return an empty list. 


Complexity:
    Time: O(n(n-m)m) where m is the length of stamp and n is the length of target
    Space: O(n)
"""


from collections import deque


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:

        # Get lengths of stamp and target
        m, n = len(stamp), len(target)

        # Convert stamp and target to lists for easier replacement
        stamp, target = list(stamp), list(target)

        # Initialize the result and a varaible to keep track of replaced characters in the target
        res, replaced = deque(), 0

        # Check if a substring of target match with the stamp
        def match(i):

            nonlocal replaced

            # Initialize two varaibles: one to track of if the two strings matched and another one to keep track of the number of replacement
            matched, count = True, 0

            # Pairs all characters
            for c1, c2 in zip(stamp, target[i : i + m]):

                # If the current character of the target is a wildcard, skip it
                if c2 == "*":
                    continue

                # Else, update the two variables
                matched &= c1 == c2
                count += int(c1 == c2)

            # If the two strings matched and we did at least 1 replacement
            if matched and count:

                # Update the substring of the target with wildstars
                target[i : i + m] = ["*"] * m

                # Add the number of replacement to the global varaible
                replaced += count

                # Add the starting index to the result
                res.appendleft(i)

            return True if matched and count else False

        changed = True

        # While we still can replace a substring of the target with the stamp
        while changed:
            changed = False

            # Check all indices of the target
            for i in range(n - m + 1):
                changed |= match(i)

        # If we replaced all characters in the target, return result. Else, return an empty list
        return list(res) if replaced == n else []

