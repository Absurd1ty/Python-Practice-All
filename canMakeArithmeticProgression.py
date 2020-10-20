"""Given an array of numbers arr. A sequence of numbers 
is called an arithmetic progression if the difference 
between any two consecutive elements is the same.

Return true if the array can be rearranged to 
form an arithmetic progression, otherwise, return false."""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort() 

         
        pattern = arr[1]  - arr[0]

        ans = True

        for i in range(1, len(arr)):
            if arr[0] + (i * pattern) != arr[i]:
                ans = False
        return ans
        