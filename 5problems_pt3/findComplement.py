"""Given a 
positive integer num, output its complement number. 
The complement strategy is to flip the bits of its binary representation.

"""

class Solution:
    def findComplement(self, num: int) -> int:
        original = bin(num)
        result = ""
        for i in str(original[2:]):
            if i == "0":
                result += "1"
            else:
                result += "0"
        return int(result,2)