"""Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest 
number of candies among them. Notice that multiple kids can have the greatest number of candies."""

class Solution:
    def kidsWithCandies(self, candies:[int], extraCandies: int):
        max = 0
        bool_arr = []
        for i in range (len(candies)):
            if candies[i] >= max:
                max = candies[i]
            else:
                continue
        for i in range (len(candies)):
            if (candies[i] + extraCandies) < max:
                bool_arr.append(False)
            else:
                bool_arr.append(True)
        return bool_arr

result = Solution().kidsWithCandies([4,2,1,1,2], 1)
print(result)
"""Runtime: 36 ms, faster than 79.17% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 14 MB, less than 93.64% of Python3 online submissions for Kids With the Greatest Number of Candies.
"""