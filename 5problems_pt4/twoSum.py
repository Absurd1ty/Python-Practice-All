"""
Given an array of integers that is 
already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers 
such that they add up to the target, where index1 must be less than index2.


"""

class Solution:
    def twoSum(self, nums: [int], target: int):

        left = 0
        right = len(nums) - 1
        
        while(left < right):
            if(nums[left] + nums[right] < target):
               
                left += 1
            if(nums[left] + nums[right] > target):
              
                right -= 1
            if((nums[left] + nums[right]) == target):
                print(nums[left])
                print(nums[right])
                return [left+1,right+1]

result = Solution().twoSum([2,7,11,15], 9)
print(result)
        