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
    We can solve this problem with backtracking. At each iteration, we will pick the next term for a proposed ip address as long as the term is valid. We know that we have a valid ip if we used all digits and we picked 4 terms and thus, we can append the proposed ip into the result. Then, we backtrack.  

Complexity:
    Time: O(3**n) 
    Space: O(3**n)

"""


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        # Find the number of digits
        n = len(s)

        # If we have too little or too many digits to form a valid ip, end the search
        if not (4 <= n <= 12):
            return []

        # Initialize the result
        res = []

        # Recursively forming valid ips
        def backtrack(i, ip):

            # If we used all digits or we have 4 terms, we end the search
            if i == n or len(ip) == 4:

                # If both conditions hold true, we have found a valid ip
                if i == n and len(ip) == 4:
                    res.append(".".join(ip))

                return

            # Else, we will pick the next term
            for j in range(i + 1, min(i + 4, n + 1)):

                # If the next term is greater than 255, end the search
                if int(s[i:j]) > 255:
                    return

                # Else, add the term into the ip
                ip.append(s[i:j])

                # Go to the next term
                backtrack(j, ip)

                # Once we return, pop the picked term from the ip
                ip.pop()

                # If there is leading 0, we will end the search after picked the first possible term
                if s[i] == "0":
                    return

        backtrack(0, [])

        return res
