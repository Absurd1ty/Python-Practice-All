"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]"."""

class Solution:
    def defangIPadrr(self, address: str): 
              return address.replace(".", "[.]")


"""Runtime: 28 ms, faster than 78.38% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 14.2 MB, less than 64.97% of Python3 online submissions for Defanging an IP Address."""


class manualSolution:
    def manual(self, address: str):
        answer = ""
        for i in address:
            if i == ".":
                answer += "[.]"
            else:
                answer +=i
        return answer

"""Runtime: 28 ms, faster than 78.38% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 14.1 MB, less than 64.97% of Python3 online submissions for Defanging an IP Address.
Same time as replace i guess. 
"""