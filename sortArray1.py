""" this was a problem in medium difficulty and i assume they wanted you to write any way to sort an array so I wrote 1 i thought of"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for i in range(n):
            
            for a in range (n - i-1):
                
                if nums[a] > nums[a+1]:
                     nums[a], nums[a+1] = nums[a+1], nums[a] 
        
        return nums 
