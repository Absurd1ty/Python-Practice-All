"""Given an array nums. We define a 
running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums."""

class Solution:
    def runningSum(self, nums: [int]):
        sum_result = []*len(nums)
        prev_sum = 0
        for i in range(len(nums)):
            prev_sum += nums[i]
            sum_result[i] = prev_sum
        return sum_result

"""Runtime: 40 ms, faster than 63.96% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.5 MB, less than 44.70% of Python3 online submissions for Running Sum of 1d Array."""