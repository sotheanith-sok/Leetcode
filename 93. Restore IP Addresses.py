"""
Problem:
    A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
    Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

    Example 1:
    Input: s = "25525511135"
    Output: ["255.255.11.135","255.255.111.35"]
    
    Example 2:
    Input: s = "0000"
    Output: ["0.0.0.0"]
    
    Example 3:
    Input: s = "101023"
    Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Solution:
    We can solve this problem with backtracking. At each iteration, we extract 1 to 3 digits from the string and append a dot at the end of it. The remaining string will be its own sub problems. We know that we found a valid ip address if we used exactly 4 dots and we reach the end of the string. Else, if we use more than 4 dots or the potential digits create value bigger than 255 or it has a leading zero, we stop and backtrack.    

Complexity:
    Time: 3**n 
    Space: 3**n

"""


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        # Since ip address is ground into 4 group of 3 digits, we couldn't generate valid ips from a string longer than 12 characters.
        if len(s) > 12:
            return []

        res = []

        def backtrack(i, dots, ip):
            # If we used 4 dots and reach the end of the string, we found a valid ip.
            # 122.555.666.777. -> 122.555.666.777
            if dots == 4 and i == len(s):
                res.append(ip[:-1])

            # If we use more than 4 dots, we won't be able to form a valid ip address
            if dots > 4:
                return

            # Recursive call for the three sub problems. min is used to prevent out of bound.
            for j in range(i, min(i + 3, len(s))):

                # Only generate a sub problem if there is no leading zero and the potential digits are less than or equal to 255. i==j ensures that a single 0 digit will be accepted.
                if int(s[i : j + 1]) <= 255 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, ip + s[i : j + 1] + ".")

        backtrack(0, 0, "")
        return res

