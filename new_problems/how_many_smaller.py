"""Given the array nums, for each nums[i] find out how many numbers 
in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]):
        result = [0] * len(nums)
        for i in range (len(nums)):
            count = 0
            for j in range (len(nums)):
                if nums[i] > nums[j]:
                     count += 1
                     result[i] = count
                else:
                    pass
        return result

"""Runtime: 496 ms, faster than 16.23% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 14.3 MB, less than 75.91% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Ok that worked but it is terrible 
"""
"""class faster:
    def smallerNumbersThanCurrent(self, nums: [int]):
        temp = sorted(nums)
        size = len(nums)
        result_arr = [0] *size
        for i in range (size):
            final_comparison = 0 
            if nums[i].count(nums[i]) > 0:
                final_comparison += nums[i].count(nums[i])
            if final_comparison > i:
                final_comparison = i
            else:
                final_comparison = i
            result_arr[i] = """    

