"""You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A"."""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str):
        jewels_count = 0
        for i in stones:
            if i in jewels:
                jewels_count += 1
            else:
                continue
        return jewels_count

"""Runtime: 36 ms, faster than 11.65% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.3 MB, less than 46.08% of Python3 online submissions for Jewels and Stones.
Apparently this is slow.
"""
class Faster:
     def numJewelsInStones(self, jewels: str, stones: str):
         jewels_count = 0
         for i in jewels:
             jewels_count += stones.count(i)
         return jewels_count
"""Runtime: 36 ms, faster than 11.65% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.1 MB, less than 74.59% of Python3 online submissions for Jewels and Stones.
Basically the same which makes sense. 
"""