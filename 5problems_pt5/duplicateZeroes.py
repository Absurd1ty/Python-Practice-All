class Solution:
    def duplicateZeros(self, arr: [int]):
        i = 0
        length = len(arr)
      
        while i < length - 1:
            if arr[i] == 0:
                currSub = arr[i+1:length-1]
                arr[i+1] = 0
                arr[i+2:length] = currSub
                i += 2
            else: i += 1
        return arr

result = Solution().duplicateZeros( [1,0,2,3,0,4,5,0])
print(result)