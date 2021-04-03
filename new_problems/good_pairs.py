"""Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.""" 

class Solution:
    def numIdenticalPairs(self, nums:[int]):
        size = len(nums)
        pair_count = 0
        for i in range (size-1):
            for j in range (i+1, size):
                if nums[i] == nums[j]:
                    pair_count += 1
        return pair_count

"""Runtime: 68 ms, faster than 5.56% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 14 MB, less than 90.56% of Python3 online submissions for Number of Good Pairs.
its a bad solution but i dont get the problem
"""