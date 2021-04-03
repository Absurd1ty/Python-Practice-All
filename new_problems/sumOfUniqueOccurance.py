"""You are given an integer array nums. 
The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

 """
class Solution:
    def sumOfUnique(self, nums: [int]):
        dictionary  = dict()
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        sum = 0
        for k, v in dictionary.items():
            
            if dictionary[k] == 1:
                sum += k
        return sum
result = Solution().sumOfUnique([1,2,3,4,5])
print(result)
