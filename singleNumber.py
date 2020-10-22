import numpy as np
"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?"""


class Solution:
    def singleNumber(self, nums: [int]):
        length = int(len(nums)/2)
        print (length)
        subarray1 = nums[0, length]
        subarray2 = nums[length+1, -1]
        return abs(sum(subarray1) - sum(subarray2))

result = Solution().singleNumber([1,1,2,2,3,3,4])    
print(result)   