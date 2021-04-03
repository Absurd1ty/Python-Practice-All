"""Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]."""

class Solution:
    def shuffle(self, nums: [int], n: int):
        shuffled = [0] *len(nums)
        index = 0 
        counter = n
        for i in range (len(nums)//2):
            shuffled[index] = nums[i]
            shuffled[index+1] = nums[counter]
            index +=2
            counter  +=1 
        return shuffled
result = Solution().shuffle([2,5,1,3,4,7], 3)

"""Runtime: 52 ms, faster than 96.13% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.5 MB, less than 50.32% of Python3 online submissions for Shuffle the Array."""