"""Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it."""

class Solution:
    def numberOfSteps (self, num: int):
        step_counter = 0 
        while num != 0:
            if num%2 == 0:
                num //= 2
                step_counter +=1
            else:
                num -= 1
                step_counter +=1
        return step_counter

"""Runtime: 24 ms, faster than 94.83% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 14.1 MB, less than 65.57% of Python3 online submissions for Number of Steps to Reduce a Number to Zero."""