"""Given two non-negative 
integers low and high. 
Return the count of odd numbers between low and high (inclusive).

"""
class Solution:
    def countOdds(self, lo, hi):
        return (hi+1)//2 - lo//2

result = Solution().countOdds(3, 5)
print(11%4)
print (result)